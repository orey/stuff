#!/bin/bash
clear

if [ $# != 3 ]
then
    echo "split-image-in-two-vertically.sh: Script version 1"
    echo "Install ImageMagick first"
    echo "Usage : split-image-in-two-vertically.sh [input-image] [percentage-of-width] [outputfilename]"
    exit 0
fi

convert -crop $2%x100% +repage $1 $3

echo $1

echo "Done"

