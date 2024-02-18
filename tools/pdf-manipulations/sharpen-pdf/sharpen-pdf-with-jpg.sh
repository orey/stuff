#!/bin/sh
clear

if [ ! -d ./sharpened ] # make sure the directory "converted" exists
then
   mkdir ./sharpened
fi

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
    convert -sharpen $2 $f ./sharpened/new_$f
    echo "Sharpened: $f"
    convert ./sharpened/new_$f ./converted/new_$f.jpg
    echo "Converted: new_$f"
    rm $f
done

convert ./converted/*.* ./$3
rm -R ./sharpened
rm -R ./converted
echo "Created $3"


