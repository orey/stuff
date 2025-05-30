#!/bin/bash
clear

if [ $# != 1 ]
then
    echo "split-image-in-two-vertically.sh: Script version 1"
    echo "Install ImageMagick first"
    echo "Usage : split-images-in-pdf-in-two.sh [input-pdf]"
    exit 0
fi

pdfimages $1 temp

for f in *.ppm
do
    echo "Rotating $f"
    convert $f -rotate 90 rotated_$f
    echo "Splitting rotated_$f"
    left="split-rotated_${f%.*}-1.ppm"
    #right="split-rotated_${f%.*}-2.ppm"
    # pages de gauche
    convert -crop 50%x100% +repage rotated_$f $left
    # pages de droite
    #convert -crop 50%x100% +repage $right $f
done

for f in split-*.ppm
do
    convert $f $f.jpg
done
    
echo "Composing PDF..."
convert split-*.jpg output.pdf

echo "Cleaning up..."
rm *.ppm
rm *.jpg

echo "Done"

