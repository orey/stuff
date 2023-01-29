#!/bin/bash

# source: https://unix.stackexchange.com/questions/15992/how-do-i-insert-a-blank-page-into-a-pdf-with-ghostscript-or-pdftk

convert xc:none -page letter blank.pdf

if [ $# -ne 2 ]
then
  echo "Usage example: ./insert-blank-page-at-same-doc src.pdf 12"
  exit $E_BADARGS
else
  pdftk A=$1 B=blank.pdf cat A1-$(($2-1)) B1 A$2-end output temp_hfgdtsgjh.pdf
fi

mv temp_hfgdtsgjh.pdf $1
rm blank.pdf



