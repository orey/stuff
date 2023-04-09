# Script that automates ocrtopdf

## Introduction

April 09 2023: After tests on several Debian machines (Debian 10 32 bits & 2 Debian 11 64 bits), it appears that `ocrtopdf` script is not working well for big PDF files (deadlocks, probably volume problems...).

This script in this folder ran in Debian 10 and 11, respectively 32 and 64 bits, for a quite large PDF (250 pages) made with rush photos and text that could be distorded (real life sample).

## Usage

The script takes a series of images in input (and not a PDF) generally obtained from the PDF by the use of `pdfimages`. This can also enable you to suppress parasit images before you reencode the PDF.

```
user@machine:~/folder$ pdfimages your_pdf.pdf key
[Potentially remove parasit images]
user@machine:~/folder$ ./process-pages "*.ppm"
```

