#!/bin/bash

# source: https://unix.stackexchange.com/questions/15992/how-do-i-insert-a-blank-page-into-a-pdf-with-ghostscript-or-pdftk

convert xc:none -page A4 blank.pdf

if [ $# -ne 3 ]
then
  echo "Usage example: ./pdfInsertBlankPageAt 5 src.pdf res.pdf"
  exit $E_BADARGS
else
  pdftk A=$2 B=blank.pdf cat A1-$(($1-1)) B1 A$1-end output $3
fi

