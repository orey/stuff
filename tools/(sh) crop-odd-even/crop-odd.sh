#!/bin/sh
clear

if [ $# != 3 ]
then
    echo "crop-odd.sh: Script version 1"
    echo "Install ImageMagick first"
    echo "Usage : crop-odd.sh [pattern] [x] [y]"
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
    w=`identify -format %w $f`
    h=`identify -format %h $f`

    # Calculate the new size after cropping
    neww=`expr $w - $2`
    newh=`expr $h - $3`

    convert $f -crop `$neww`x$newh+$2+$3 +repage ./output/$f

    echo "$f converted"
done   

echo "Done"

#170,200

