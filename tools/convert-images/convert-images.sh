#!/bin/sh
clear

if [ ! -d ./converted ] # make sure the directory "converted" exists
then
   mkdir ./converted
fi

if [ $# != 2 ]
then
    echo "convert-images.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : convert-images.sh [sourceformat] [targetformat]"
    exit 0
fi

for f in *.$1
do
    new="${f%.*}.$2"
    convert $f ./converted/$new
    echo "$f converted into ./converted/$new"
done

