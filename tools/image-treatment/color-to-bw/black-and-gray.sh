#!/bin/bash

clear

if [ $# != 1 ]
then
  echo "compress-pdf.sh: Script version 1"
  echo "Usage : black-and-white.sh [name-of-pdf-without-pdf-extension]"
  exit 0
fi

gs -dSAFER -dBATCH -dNOPAUSE -r150 -sDEVICE=pnggray -dTextAlphaBits=4  -sOutputFile=doc-%03d.png $1.pdf

convert doc-*.png $1-bw.pdf

rm doc-*.png
