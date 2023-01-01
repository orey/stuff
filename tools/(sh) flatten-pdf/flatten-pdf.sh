#!/bin/bash
clear

if [ $# != 1 ]
then
    echo "flatten-pdf.sh: Script version 1"
    echo "Install pdf2ps and ps2pdf first"
    echo "Usage : flatten-pdf.sh [file.pdf]"
    echo "Produce an output file named file-flattened.pdf"
    exit 0
fi

pdf2ps "$1" - | ps2pdf - "flattened-$1"

echo "Done"

