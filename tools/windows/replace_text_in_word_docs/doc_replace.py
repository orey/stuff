#!/usr/bin/env python3
"""
docx_replace.py
---------------
Replace $TAG$ placeholders in Word .docx template files, driven by an .ini
config file.

Usage:
    python docx_replace.py <config.ini>

Config file layout
==================
[templates]
    One line per template:
        <template .docx (full path)> = <output .docx (full path)>
    Templates are never modified; the result is written to the output path.
    Add as many lines as you like.

[tags]
    One line per tag:
        <tag name> = <replacement text>
    The tag name is the text between the two $ signs in the document,
    WITHOUT the $ signs themselves.
    e.g. document contains:  Dear $CLIENT_NAME$,
         config line is:     CLIENT_NAME = Acme Corporation

Tags present in a document but absent from [tags] are left unchanged
and reported as warnings.
"""

import configparser
import re
import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.text.run import Run

TAG_RE = re.compile(r"\$([^$]+)\$")


# ---------------------------------------------------------------------------
# Paragraph iteration: body, tables (incl. nested), headers and footers
# ---------------------------------------------------------------------------
def iter_paragraphs(container):
    """Yield every Paragraph inside *container*, recursing into tables."""
    for block in container.iter_inner_content():
        if isinstance(block, Paragraph):
            yield block
        elif isinstance(block, Table):
            for row in block.rows:
                for cell in row.cells:
                    yield from iter_paragraphs(cell)


def iter_all_paragraphs(doc):
    """Yield every paragraph of the document body and of all headers/footers."""
    yield from iter_paragraphs(doc._body)
    for section in doc.sections:
        for part in (
            section.header,
            section.footer,
            section.first_page_header,
            section.first_page_footer,
            section.even_page_header,
            section.even_page_footer,
        ):
            yield from iter_paragraphs(part)


# ---------------------------------------------------------------------------
# Replacement (works even when a tag is split across several runs)
# ---------------------------------------------------------------------------
def replace_tags_in_paragraph(paragraph, values):
    """
    Replace every $TAG$ occurrence in the paragraph.
    The replacement text keeps the formatting of the run where the tag starts.
    Returns (replaced_tags, missing_tags) as lists of tag names.
    """
    runs = [Run(r, paragraph) for r in paragraph._p.iter(qn("w:r"))]
    if not runs:
        return [], []

    full_text = "".join(run.text for run in runs)
    if "$" not in full_text:
        return [], []

    # Absolute character offset of each run inside full_text
    offsets = []
    pos = 0
    for run in runs:
        offsets.append((run, pos, pos + len(run.text)))
        pos += len(run.text)

    replaced, missing = [], []
    for match in TAG_RE.finditer(full_text):
        tag = match.group(1)
        start, end = match.span()

        if tag not in values:
            missing.append(tag)
            continue

        replacement = values[tag]
        first = True
        for run, r_start, r_end in offsets:
            if r_end <= start or r_start >= end:
                continue  # this run is not touched by the tag
            lo = max(start, r_start) - r_start
            hi = min(end, r_end) - r_start
            if first:
                # keep the text before the tag, then insert the replacement
                run.text = run.text[:lo] + replacement
                first = False
            else:
                # drop the tag characters, keep any trailing text
                run.text = run.text[hi:]
        replaced.append(tag)

    return replaced, missing


def process_template(template_path, output_path, values):
    template_path = Path(template_path)
    output_path = Path(output_path)

    if template_path.resolve() == output_path.resolve():
        raise ValueError("output path is the same as the template path")

    doc = Document(str(template_path))
    replaced, missing = [], []
    for paragraph in iter_all_paragraphs(doc):
        rep, mis = replace_tags_in_paragraph(paragraph, values)
        replaced.extend(rep)
        missing.extend(mis)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(output_path))
    return replaced, missing


# ---------------------------------------------------------------------------
# Optional PDF export (same file name, .pdf extension)
# ---------------------------------------------------------------------------
def pdf_with_word(docx_path):
    """Convert using Microsoft Word (Windows, best fidelity)."""
    import win32com.client  # pip install pywin32

    word = win32com.client.DispatchEx("Word.Application")  # own instance
    word.Visible = False
    try:
        doc = word.Documents.Open(str(docx_path.resolve()), ReadOnly=True)
        try:
            doc.SaveAs(str(docx_path.with_suffix(".pdf")), FileFormat=17)  # 17 = wdFormatPDF
        finally:
            doc.Close(False)
    finally:
        word.Quit()


def pdf_with_libreoffice(docx_path):
    """Convert using LibreOffice headless (free, cross-platform)."""
    import shutil
    import subprocess

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice and sys.platform == "win32":
        for candidate in (
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
        ):
            if Path(candidate).exists():
                soffice = candidate
                break
    if not soffice:
        raise FileNotFoundError("no Microsoft Word or LibreOffice available for PDF export")

    subprocess.run(
        [soffice, "--headless", "--convert-to", "pdf",
         "--outdir", str(docx_path.parent), str(docx_path)],
        check=True,
        capture_output=True,
        timeout=180,
    )


def make_pdf(docx_path):
    """Create docx_path with a .pdf extension. Returns a status string."""
    pdf_path = docx_path.with_suffix(".pdf")
    try:
        if sys.platform == "win32":
            try:
                pdf_with_word(docx_path)
                if pdf_path.exists():
                    return "ok (Microsoft Word)"
            except Exception:
                pass  # fall back to LibreOffice
        pdf_with_libreoffice(docx_path)
        if pdf_path.exists():
            return "ok (LibreOffice)"
        raise RuntimeError("converter finished but the PDF was not found")
    except Exception as exc:
        return f"FAILED: {exc}"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main(argv):
    make_pdf_enabled = "--no-pdf" not in argv
    args = [a for a in argv[1:] if a != "--no-pdf"]
    if len(args) != 1:
        print(__doc__)
        return 2

    ini_path = Path(args[0])
    if not ini_path.is_file():
        print(f"Error: config file not found: {ini_path}")
        return 1

    parser = configparser.ConfigParser(interpolation=None, delimiters=('='))  # allow % in values
    parser.optionxform = str                                # keep tag case as typed
    with open(ini_path, encoding="utf-8-sig") as fh:
        parser.read_file(fh)

    if "templates" not in parser or not parser["templates"]:
        print("Error: the [templates] section is missing or empty.")
        return 1

    values = {k.strip(): v.strip() for k, v in parser["tags"].items()} \
        if "tags" in parser else {}
    if not values:
        print("Warning: no [tags] section (or it is empty); nothing will be replaced.")

    exit_code = 0
    used = set()
    for template, output in parser["templates"].items():
        print(f"\nTemplate : {template}")
        if not Path(template).is_file():
            print("  ERROR: template file not found.")
            exit_code = 1
            continue
        try:
            replaced, missing = process_template(template, output, values)
        except Exception as exc:
            print(f"  ERROR: {exc}")
            exit_code = 1
            continue

        used.update(replaced)
        print(f"  Output   : {output}")
        if make_pdf_enabled:
            print(f"  PDF      : {Path(output).with_suffix('.pdf')} "
                  f"{make_pdf(Path(output))}")
        print(f"  Replaced : {len(replaced)} placeholder(s)")
        for tag in sorted(set(missing)):
            print(f"  WARNING: ${tag}$ has no value in [tags]; left unchanged.")

    for tag in sorted(set(values) - used):
        print(f"NOTE: tag '{tag}' from [tags] was not found in any template.")

    return exit_code

if __name__ == "__main__":
    sys.exit(main(sys.argv))

    
