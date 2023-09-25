#!/bin/sh
clear

if [ ! -d ./output ] # make sure the directory "output" exists
then
   mkdir ./output
fi

if [ $# != 3 ]
then
    echo "resize-images.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Does not resize the image if width and height are already OK"
    echo "Usage : resize.sh [pattern] [width] [height]"
    echo "Sample of pattern (put double quotes around it): *.JPG, myimages*.png"
    echo "width and height must be integers"
    exit 0
fi

for f in $1
do 
    w=`identify -format %w "$f"`
    h=`identify -format %h "$f"`
    if [ $w -eq $2 ] && [ $h -eq $3 ]
    then
        echo "$f: $wx$h - Not converted, already in a good format"
        cp "$f" "./output/$f"
    else
        convert "$f" -resize $2x$3! "./output/$f"
        echo "$f: $wx$h - Converted"
    fi
done

