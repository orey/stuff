#!/bin/bash
clear

if [ $# != 1 ]
then
    echo "Usage : script.sh [image]"
    echo "Splits in half, convert to PDF"
    exit 0
fi

f=$1

echo "Splitting $1"
left="${f%.*}.png"
convert -crop 50%x100% +repage $1 $left

result0=${f%.*}-0.png
result1=${f%.*}-1.png

img2pdf $result0 $result1 -o ${f%.*}.pdf

echo "Done"

