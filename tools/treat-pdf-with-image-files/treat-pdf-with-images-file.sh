#!/bin/sh
clear

if [ $# != 2 ]
then
    echo "treat-pdf-with-images-file.sh: Script version 1"
    echo "Requires: pdfimages and Imagemagick (convert) to be installed"
    echo "Usage : treat-pdf-with-images-file.sh [in.pdf] [out.pdf]"
    exit 0
fi

echo "Extracting images from input pdf"
pdfimages $1 temp1

for f in *.ppm
do
    echo "Processing $f"
    # resize
    convert $f -resize 48% temp2-$f
    # remove grey background
    convert temp2-$f -fill white -fuzz 80% +opaque "#000000" temp3-$f
    # sharpen argument can be anything between 0.1 and 3
    convert temp3-$f -sharpen 0x2.5 temp-$f
done

echo "Creating PDF document"
convert -bordercolor none -border 10 temp-*.ppm $2

echo "Removing temporary files"
rm temp*.ppm

echo "Done"

