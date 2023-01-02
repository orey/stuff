#!/bin/bash
clear

if [ $# != 1 ]
then
    echo "Usage : script.sh [image]"
    echo "Splits in half, convert to greyscale, invert colors and transforms in PDF"
    exit 0
fi

f=$1

echo "Splitting $1"
left="${f%.*}.png"
convert -crop 50%x100% +repage $1 $left

result0=${f%.*}-0.png
result1=${f%.*}-1.png

new0=${f%.*}-0-gray.png
new1=${f%.*}-1-gray.png

convert $result0 -set colorspace Gray -separate -average $new0
convert $result1 -set colorspace Gray -separate -average $new1

inv0="${f%.*}-0-gray-inverted.png"
inv1="${f%.*}-1-gray-inverted.png"

convert $new0 -channel RGB -negate $inv0
convert $new1 -channel RGB -negate $inv1

img2pdf $inv0 -o cover2.pdf
img2pdf $inv1 -o cover1.pdf

echo "Done"

