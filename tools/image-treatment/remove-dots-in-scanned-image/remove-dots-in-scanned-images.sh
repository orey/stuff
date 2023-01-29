#!/bin/sh
clear

if [ ! -d ./output ] # make sure the directory "output" exists
then
    mkdir ./output
else
    rm -R ./output
    mkdir ./output
fi

if [ $# != 0 ]
then
    echo "remove-dots-in-scanned-images.sh: Script version 1"
    echo "Cleans all images"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : remove-dots-in-scanned-images.sh"
    exit 0
fi

for f in *.pbm
do 
    python3 remove-dots.py $f output
    echo "$f: done"
done

