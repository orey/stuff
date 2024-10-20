#!/bin/sh
clear

if [ ! -d ./converted ] # make sure the directory "converted" exists
then
   mkdir ./converted
fi

if [ $# != 3 ]
then
    echo "sharpen-pdf.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : sharpen-pdf.sh [input.pdf] [0x4] [output.pdf]"
    exit 0
fi

pdfimages $1 temp

for f in *.ppm
do
    convert -sharpen $2 $f ./converted/new_$f
    echo "Converting $f"
    rm $f
done

convert ./converted/*.* ./$3
rm -R ./converted
echo "Created $3"


