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

cut-in-half () {
    for f in *.$1
    do
        echo "Splitting $f"
        convert $f -crop 2x1@ +repage +adjoin $f-%d.jpg
    done
}

cut-in-half "ppm"
cut-in-half "pbm"

echo "Composing PDF..."
img2pdf *.jpg -o output.pdf
    
echo "Cleaning up..."
rm *.ppm
rm *.pbm
rm *.jpg

echo "Done"

