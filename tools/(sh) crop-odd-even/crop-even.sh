#!/bin/sh
clear

if [ $# != 3 ]
then
    echo "crop-even.sh: Script version 1"
    echo "Install ImageMagick first"
    echo "Usage : crop-even.sh [pattern] [x] [y]"
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
    newh=`expr $h - $3`


    convert $f -crop $2x$newh+0+$3 +repage ./output/$f

    echo "$f converted"
done   

echo "Done"


