#!/bin/bash

clear

if [ $# != 1 ]
then
  echo "compress-pdf.sh: Script version 1"
  echo "Usage : black-and-white.sh [name-of-pdf-without-pdf-extension]"
  exit 0
fi

echo "=========================="
echo "Extracting B&W PNG"
echo "=========================="
#gs -dSAFER -dBATCH -dNOPAUSE -r150 -sDEVICE=pngmono -dTextAlphaBits=4  -sOutputFile=doc-%03d.png $1.pdf
gs -dSAFER -dBATCH -dNOPAUSE -r300 -sDEVICE=pngmono -dTextAlphaBits=4  -sOutputFile=doc-%03d.png $1.pdf

echo "=========================="
echo "Creating B&W PDF"
echo "=========================="
convert doc-*.png $1-bw.pdf

echo "=========================="
echo "Removing B&W PNG"
echo "=========================="
rm doc-*.png

#echo "=========================="
#echo "Creation screen version"
#echo "=========================="
#gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dBATCH -sOutputFile=$1-bw-screen.pdf $1-bw.pdf

echo "=========================="
echo "Creation ebook version"
echo "=========================="
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dBATCH -sOutputFile=$1-bw-ebook.pdf $1-bw.pdf

