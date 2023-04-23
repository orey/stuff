#!/bin/sh
clear

if [ $# != 1 ]
then
    echo "analyze-image.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : analyze-image.sh [image]"
    exit 0
fi

echo "Current resolution is:"
identify -format '%x,%y\n' $1

w=`identify -format %w $f`
h=`identify -format %h $f`
echo "Size of image: width= $w / height= $h"

