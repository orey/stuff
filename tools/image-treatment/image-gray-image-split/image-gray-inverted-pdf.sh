#!/bin/bash
clear

if [ $# != 1 ]
then
    echo "Usage : script.sh [image]"
    echo "Splits in half, convert to greyscale, invert colors and transforms in PDF"
    exit 0
fi

f=$1

new0=${f%.*}-gray.png

convert $f -set colorspace Gray -separate -average $new0

inv0="${f%.*}-gray-inverted.png"

convert $new0 -channel RGB -negate $inv0

img2pdf $inv0 -o ${f%.*}.pdf

echo "Done"

