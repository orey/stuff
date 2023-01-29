#!/bin/bash
clear

if [ $# -eq 0 ]
then
    echo "rotate-images.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : rotate-images.sh [pattern] [angle]"
    echo "Pattern can be *.png between double quotes"
    exit 0
fi

# Le but est de trouver le nom de l'image à retourner
# décalage de 1 car pdfimages commence à 0 + padde à trois chiffres

for f in $1
do
    # anticlockwise
    convert $f -rotate $2 rotated-$f.png
    echo "Created rotated-$f.png"
done

echo "Done"


