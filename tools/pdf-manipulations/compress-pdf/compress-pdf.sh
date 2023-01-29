#!/bin/bash

clear

if [ $# != 1 ]
then
  echo "compress-pdf.sh: Script version 1"
  echo "Usage : compress-pdf.sh [name-of-pdf-without-pdf-extension]"
  exit 0
fi

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$1-compressed.pdf $1.pdf
