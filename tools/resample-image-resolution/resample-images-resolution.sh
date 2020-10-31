#!/bin/sh
clear

if [ ! -d ./resampled ] # make sure the directory "output" exists
then
   mkdir ./resampled
fi

if [ $# != 3 ]
then
    echo "resample-images-resolution.sh: Script version 1"
    echo "Set all images to the same resolution"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : resample-images-resolution.sh [pattern] [resolution-x] [resolution-y]"
    echo "Sample of pattern (put double quotes around it): *.JPG, myimages*.png"
    echo "Margins must be integers"
    exit 0
fi

for f in $1
do 
    # Blank should be added
    convert $f -resample $2x$3 ./resampled/$f
    echo "$f: Resampled in resampled directory"
done

