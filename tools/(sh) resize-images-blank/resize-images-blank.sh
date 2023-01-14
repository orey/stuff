#!/bin/sh
clear

if [ ! -d ./output ] # make sure the directory "output" exists
then
   mkdir ./output
fi

if [ $# != 3 ]
then
    echo "resize-images-blank.sh: Script version 1"
    echo "Add margins in pixels. Warning margin is added left and right, and top and bottom"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : resize-images-blank.sh [pattern] [margin-width] [margin-height]"
    echo "Sample of pattern (put double quotes around it): *.JPG, myimages*.png"
    echo "Margins must be integers"
    exit 0
fi

for f in $1
do 
    # Blank should be added
    convert $f -bordercolor white -border $2x$3 ./output/$f
    echo "$f: Converted in output directory"
done

