#!/bin/bash
clear

if [ $# -eq 0 ]
then
    echo "convert-images-to-gray-scale.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : convert-images-to-grey-scale.sh [pattern]"
    echo "Pattern can be *.png between double quotes"
    exit 0
fi

for f in $1
do
    new="${f%.*}-gray.png"
    convert $f -set colorspace Gray -separate -average $new
    echo "Created image $new"
done

echo "Done"


