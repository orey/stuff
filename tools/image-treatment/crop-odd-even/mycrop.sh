#!/bin/sh

if [ $# != 5 ]
then
    echo "crop-even.sh: Script version 1"
    echo "Install ImageMagick first"
    echo "Usage : crop-even.sh [pattern] [x] [y] [w] [h]"
    echo "Sample of pattern (put double quotes around it): *.JPG, myimages*.png"
    exit 0
fi

if [ ! -d ./output ] # make sure the directory "output" exists
then
   mkdir ./output
fi

for f in $1
do 
    # Find the size of each image
    ww=`identify -format %w $f`
    hh=`identify -format %h $f`

    echo "Image format: $ww x $hh"

    convert $f -crop $4x$5+$2+$3 +repage ./output/$f

    echo "$f converted"
done   

echo "Done"


