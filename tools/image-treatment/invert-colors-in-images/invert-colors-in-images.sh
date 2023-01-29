#!/bin/bash
clear

if [ $# -eq 0 ]
then
    echo "invert-colors-in-images.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : invert-colors-in-images.sh [pattern]"
    echo "Pattern can be *.png between double quotes"
    exit 0
fi

for f in $1
do
    new="${f%.*}-inverted.png"
    convert $f -channel RGB -negate $new
    echo "Created image $new"
done

echo "Done"


