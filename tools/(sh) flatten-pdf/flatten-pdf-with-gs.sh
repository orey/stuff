#!/bin/bash
clear

if [ $# != 1 ]
then
    echo "flatten-pdf.sh: Script version 1"
    echo "Install gs first"
    echo "Usage : flatten-pdf.sh [file.pdf]"
    echo "Produce an output file named flat-file.pdf"
    exit 0
fi

gs -dSAFER -dBATCH -dNOPAUSE -dNOCACHE -sDEVICE=pdfwrite \
   -dPDFSETTINGS=/prepress \
   -dPreserveAnnots=false \
   -sOutputFile=flat-$1 $1

echo "Done"

