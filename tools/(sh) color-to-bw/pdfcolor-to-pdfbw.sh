#!/bin/bash
# 
# $ sudo apt install poppler-utils img2pdf pdftk imagemagick
#
# Output is still greyscale, but lots of scanner light tone fuzz removed.
#
clear

if [ $# != 1 ]
then
    echo "pdfcolor-to-pdfbw.sh: Script version 1"
    echo "Requires: ghostscript to be installed"
    echo "Usage : pdfcolor-to-pdfbw.sh [pdfname]"
    exit 0
fi

#!/bin/bash

gs \
 -sOutputFile=$1_bw.pdf \
 -sDEVICE=pdfwrite \
 -sColorConversionStrategy=Gray \
 -dProcessColorModel=/DeviceGray \
 -dCompatibilityLevel=1.4 \
 -dNOPAUSE \
 -dBATCH \
 $1

echo "Done"

