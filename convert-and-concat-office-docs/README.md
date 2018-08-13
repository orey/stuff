# convert-and-concat-office-docs

Small shell script using LibreOffice to convert and concat Office documents

## Story

Sometimes, in certain projects, you arrive after a large number of documents were written.

Provided those documents are named in a chronological way, provided you have `LibreOffice` installed and `pdfunite` installed on your Linux machine, you can generate a big PDF document from a set of `docx` or `pptx` using the command line conversion facility of LibreOffice (not so documented).

For sure, some layouts may be a bit different from the original `docx` and `pptx` documents, but it can be much easier to read and transport.

## Usage

    convert-and-concat.sh [file-type]

The script will create a folder `_converted` with the consolidated pdf in it.

Note that you can run:

    convert-and-concat.sh docx
    convert-and-concat.sh pptx

in the same folder, generating a `merged-docx-documents.pdf` and a `merged-pptx-documents.pdf` file.





