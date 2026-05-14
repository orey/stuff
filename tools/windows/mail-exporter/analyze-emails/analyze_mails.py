# =============================================================================
# analyze_mails.py
#
# Nightly pipeline that:
#   1. Scans all dated day-folders under EXPORT_ROOT
#   2. Parses each .txt mail file (metadata + body)
#   3. Extracts text from PDF and Word attachments
#   4. Deduplicates threads (keeps most recent mail per ConversationID)
#   5. Flags mails from important senders
#   6. Calls the Anthropic API for per-thread summaries + a global digest
#   7. Writes a Markdown report
#
# Requirements:
#   pip install anthropic pdfplumber python-docx
# =============================================================================

import os
import re
import json
import time
import logging
from datetime import datetime, date
from pathlib import Path
from typing import Optional

import anthropic
import pdfplumber
from docx import Document as DocxDocument

# =============================================================================
# CONFIGURATION — edit this section
# =============================================================================

# Root folder where VBA exports day-subfolders (e.g. C:\MailExport\2026-05-12\)
EXPORT_ROOT = r"C:\MailExport"

# Where to write the output Markdown report
REPORT_OUTPUT = r"C:\MailExport\digest.md"

# Your Anthropic API key (or set the ANTHROPIC_API_KEY environment variable)
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# Model to use
MODEL = "claude-sonnet-4-20250514"

# Important senders — exact addresses and/or domains
IMPORTANT_EMAILS = {
    # "boss@company.com",
    # "cto@company.com",
}
IMPORTANT_DOMAINS = {
    # "client.com",
    # "partner.org",
}

# Maximum characters of mail content to send to the API per thread
# (keeps token usage bounded; ~4 chars per token)
MAX_CHARS_PER_THREAD = 8000

# Maximum characters of attachment text to append per attachment
MAX_CHARS_PER_ATTACHMENT = 3000

# Pause between API calls (seconds) to avoid rate-limit bursts
API_CALL_PAUSE = 1.0

# =============================================================================
# END OF CONFIGURATION
# =============================================================================

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)s  %(message)s")
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

class Mail:
    """Represents one parsed .txt mail file."""

    def __init__(self):
        self.file_path: str = ""
        self.from_addr: str = ""
        self.from_name: str = ""
        self.to: str = ""
        self.cc: str = ""
        self.date: Optional[datetime] = None
        self.subject: str = ""
        self.conversation_id: str = ""
        self.conversation_topic: str = ""
        self.importance: str = "Normal"
        self.has_attachments: bool = False
        self.attachment_filenames: list[str] = []   # filenames listed in header
        self.body: str = ""
        self.attachment_texts: dict[str, str] = {}  # filename -> extracted text
        self.is_important: bool = False

    def full_content(self) -> str:
        """Assembles metadata + body + attachment excerpts into one string."""
        parts = [
            f"FROM: {self.from_name} <{self.from_addr}>",
            f"DATE: {self.date.strftime('%Y-%m-%d %H:%M') if self.date else '?'}",
            f"SUBJECT: {self.subject}",
            f"TO: {self.to}",
        ]
        if self.cc:
            parts.append(f"CC: {self.cc}")
        parts.append("")
        parts.append(self.body[:MAX_CHARS_PER_THREAD])

        for fname, text in self.attachment_texts.items():
            parts.append(f"\n--- ATTACHMENT: {fname} ---")
            parts.append(text[:MAX_CHARS_PER_ATTACHMENT])

        return "\n".join(parts)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_mail_file(file_path: str) -> Optional[Mail]:
    """
    Reads a .txt file produced by ExportMails.bas and returns a Mail object.
    The file format is:
        KEY:   value
        ...
        ATTACHMENTS:
          filename1
          filename2
        ---...---   (separator line of dashes)
        body text
    """
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            raw = f.read()
    except Exception as e:
        log.warning(f"Cannot read {file_path}: {e}")
        return None

    mail = Mail()
    mail.file_path = file_path

    # Split on the dash separator line
    sep_match = re.search(r"^-{40,}", raw, re.MULTILINE)
    if sep_match:
        header_part = raw[:sep_match.start()]
        mail.body = raw[sep_match.end():].strip()
    else:
        header_part = raw
        mail.body = ""

    # Parse header fields
    in_attachments_block = False
    for line in header_part.splitlines():
        # Attachment list lines (indented)
        if in_attachments_block:
            stripped = line.strip()
            if stripped and not re.match(r"^[A-Z\-]+:", line):
                # Skip error lines starting with "!"
                if not stripped.startswith("!"):
                    mail.attachment_filenames.append(stripped)
                continue
            else:
                in_attachments_block = False  # fall through to normal parsing

        if line.startswith("FROM:"):
            mail.from_addr = line.split(":", 1)[1].strip()
        elif line.startswith("FROM-NAME:"):
            mail.from_name = line.split(":", 1)[1].strip()
        elif line.startswith("TO:"):
            mail.to = line.split(":", 1)[1].strip()
        elif line.startswith("CC:"):
            mail.cc = line.split(":", 1)[1].strip()
        elif line.startswith("DATE:"):
            raw_date = line.split(":", 1)[1].strip()
            try:
                mail.date = datetime.strptime(raw_date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                pass
        elif line.startswith("SUBJECT:"):
            mail.subject = line.split(":", 1)[1].strip()
        elif line.startswith("CONVERSATION-ID:"):
            mail.conversation_id = line.split(":", 1)[1].strip()
        elif line.startswith("CONVERSATION-TOPIC:"):
            mail.conversation_topic = line.split(":", 1)[1].strip()
        elif line.startswith("IMPORTANCE:"):
            mail.importance = line.split(":", 1)[1].strip()
        elif line.startswith("HAS-ATTACHMENTS:"):
            val = line.split(":", 1)[1].strip().lower()
            mail.has_attachments = val in ("true", "yes", "1")
        elif line.startswith("ATTACHMENTS:"):
            in_attachments_block = True

    return mail


# ---------------------------------------------------------------------------
# Attachment text extraction
# ---------------------------------------------------------------------------

def extract_pdf_text(file_path: str) -> str:
    """Extracts plain text from a PDF using pdfplumber."""
    try:
        with pdfplumber.open(file_path) as pdf:
            pages = [page.extract_text() or "" for page in pdf.pages]
        return "\n".join(pages).strip()
    except Exception as e:
        return f"[PDF extraction failed: {e}]"


def extract_docx_text(file_path: str) -> str:
    """Extracts plain text from a .docx file."""
    try:
        doc = DocxDocument(file_path)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n".join(paragraphs).strip()
    except Exception as e:
        return f"[DOCX extraction failed: {e}]"


def attach_extracted_texts(mail: Mail, folder: str):
    """
    For each attachment filename listed in the mail header,
    tries to extract text if it is a PDF or Word file.
    """
    for fname in mail.attachment_filenames:
        full_path = os.path.join(folder, fname)
        if not os.path.isfile(full_path):
            continue
        lower = fname.lower()
        if lower.endswith(".pdf"):
            mail.attachment_texts[fname] = extract_pdf_text(full_path)
        elif lower.endswith(".docx") or lower.endswith(".doc"):
            mail.attachment_texts[fname] = extract_docx_text(full_path)
        # Other types are silently ignored


# ---------------------------------------------------------------------------
# Importance detection
# ---------------------------------------------------------------------------

def check_importance(mail: Mail):
    """Sets mail.is_important based on sender address / domain."""
    addr = mail.from_addr.lower().strip()
    if addr in {e.lower() for e in IMPORTANT_EMAILS}:
        mail.is_important = True
        return
    for domain in IMPORTANT_DOMAINS:
        if addr.endswith("@" + domain.lower().lstrip("@")):
            mail.is_important = True
            return
    mail.is_important = False


# ---------------------------------------------------------------------------
# Thread deduplication
# ---------------------------------------------------------------------------

def deduplicate_threads(mails: list[Mail]) -> list[Mail]:
    """
    Groups mails by ConversationID.
    Within each group, keeps only the most recent mail.
    Mails without a ConversationID are kept as-is.
    """
    threads: dict[str, list[Mail]] = {}
    no_thread: list[Mail] = []

    for mail in mails:
        cid = mail.conversation_id.strip()
        if cid:
            threads.setdefault(cid, []).append(mail)
        else:
            no_thread.append(mail)

    result: list[Mail] = []
    for cid, group in threads.items():
        # Sort by date descending, pick the first (most recent)
        group.sort(key=lambda m: m.date or datetime.min, reverse=True)
        result.append(group[0])

    result.extend(no_thread)

    # Sort final list by date ascending for the report
    result.sort(key=lambda m: m.date or datetime.min)
    return result


# ---------------------------------------------------------------------------
# Folder scanning
# ---------------------------------------------------------------------------

def scan_export_root(root: str) -> list[Mail]:
    """
    Walks EXPORT_ROOT looking for dated subfolders (YYYY-MM-DD).
    Parses all .txt files found in them.
    Returns a flat list of Mail objects.
    """
    all_mails: list[Mail] = []
    root_path = Path(root)

    if not root_path.exists():
        log.error(f"Export root does not exist: {root}")
        return []

    folder_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    day_folders = sorted([
        d for d in root_path.iterdir()
        if d.is_dir() and folder_pattern.match(d.name)
    ])

    if not day_folders:
        log.warning("No dated day-folders found under " + root)
        return []

    log.info(f"Found {len(day_folders)} day folder(s) to process.")

    for day_folder in day_folders:
        txt_files = sorted(day_folder.glob("*.txt"))
        log.info(f"  {day_folder.name}: {len(txt_files)} .txt file(s)")

        for txt_file in txt_files:
            mail = parse_mail_file(str(txt_file))
            if mail is None:
                continue
            attach_extracted_texts(mail, str(day_folder))
            check_importance(mail)
            all_mails.append(mail)

    return all_mails


# ---------------------------------------------------------------------------
# API calls
# ---------------------------------------------------------------------------

def call_api(client: anthropic.Anthropic, system_prompt: str, user_content: str) -> str:
    """Calls the Anthropic API and returns the text response."""
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=1000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_content}],
        )
        return response.content[0].text.strip()
    except Exception as e:
        log.error(f"API call failed: {e}")
        return f"[API error: {e}]"


THREAD_SUMMARY_SYSTEM = """You are an executive assistant summarizing business emails.
For the email thread provided, write a concise summary (3-5 bullet points) covering:
- What the thread is about
- Key decisions or requests
- Any action items or deadlines
- Who the main participants are
Be factual and concise. Use plain Markdown bullet points."""


GLOBAL_DIGEST_SYSTEM = """You are an executive assistant producing a morning email digest.
You will receive a list of thread summaries. Your job is to:
1. Write a short overall summary (2-3 sentences) of the day's email activity
2. Highlight the top 3-5 most important or urgent items across all threads
3. List any action items that require a response or decision

Be concise, factual, and use plain Markdown. Do not repeat thread summaries verbatim."""


def summarize_thread(client: anthropic.Anthropic, mail: Mail) -> str:
    """Generates a summary for a single mail/thread."""
    time.sleep(API_CALL_PAUSE)
    return call_api(client, THREAD_SUMMARY_SYSTEM, mail.full_content())


def generate_global_digest(client: anthropic.Anthropic, thread_summaries: list[dict]) -> str:
    """Generates the top-level digest from all thread summaries."""
    # Build a compact input: one block per thread
    blocks = []
    for ts in thread_summaries:
        label = "⭐ IMPORTANT — " if ts["important"] else ""
        blocks.append(
            f"### {label}{ts['subject']}\n"
            f"From: {ts['from']}\n"
            f"Date: {ts['date']}\n"
            f"{ts['summary']}"
        )
    combined = "\n\n---\n\n".join(blocks)
    time.sleep(API_CALL_PAUSE)
    return call_api(client, GLOBAL_DIGEST_SYSTEM, combined)


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def write_report(
    output_path: str,
    mails: list[Mail],
    thread_summaries: list[dict],
    global_digest: str,
):
    """Writes the final Markdown report."""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    important_count = sum(1 for m in mails if m.is_important)
    thread_count = len(mails)

    lines = [
        f"# Email Digest — generated {now_str}",
        "",
        f"**Threads analyzed:** {thread_count}  |  "
        f"**Important senders:** {important_count}",
        "",
        "---",
        "",
        "## Overall Summary",
        "",
        global_digest,
        "",
        "---",
        "",
        "## Thread Summaries",
        "",
    ]

    # Important threads first, then the rest
    sorted_summaries = sorted(thread_summaries, key=lambda x: (not x["important"], x["date"]))

    for ts in sorted_summaries:
        star = "⭐ " if ts["important"] else ""
        lines.append(f"### {star}{ts['subject']}")
        lines.append(f"*From: {ts['from']} — {ts['date']}*")
        if ts.get("attachments"):
            lines.append(f"*Attachments: {', '.join(ts['attachments'])}*")
        lines.append("")
        lines.append(ts["summary"])
        lines.append("")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    log.info(f"Report written to: {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    log.info("=== Mail analysis pipeline starting ===")

    if not ANTHROPIC_API_KEY:
        log.error("ANTHROPIC_API_KEY is not set. Export it as an environment variable or set it in the script.")
        return

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # 1. Scan all day folders and parse mails
    all_mails = scan_export_root(EXPORT_ROOT)
    if not all_mails:
        log.warning("No mails found. Nothing to do.")
        return
    log.info(f"Total mails parsed: {len(all_mails)}")

    # 2. Deduplicate threads
    mails = deduplicate_threads(all_mails)
    log.info(f"After deduplication: {len(mails)} thread(s)")

    # 3. Summarize each thread via API
    thread_summaries = []
    for i, mail in enumerate(mails, 1):
        log.info(f"  [{i}/{len(mails)}] Summarizing: {mail.subject[:60]}")
        summary = summarize_thread(client, mail)
        thread_summaries.append({
            "subject":     mail.subject or "(no subject)",
            "from":        f"{mail.from_name} <{mail.from_addr}>",
            "date":        mail.date.strftime("%Y-%m-%d %H:%M") if mail.date else "?",
            "important":   mail.is_important,
            "attachments": list(mail.attachment_texts.keys()),
            "summary":     summary,
        })

    # 4. Generate global digest
    log.info("Generating global digest...")
    global_digest = generate_global_digest(client, thread_summaries)

    # 5. Write report
    write_report(REPORT_OUTPUT, mails, thread_summaries, global_digest)

    log.info("=== Pipeline complete ===")


if __name__ == "__main__":
    main()
