#!/bin/sh
clear

if [ ! -d ./output ] # make sure the directory "output" exists
then
   mkdir ./output
fi

if [ $# != 1 ]
then
    echo "process-pages.sh: Script version 1"
    echo "Usage : process-pages.sh [pattern]"
    echo "Sample of pattern (put double quotes around it): *.JPG, myimages*.png"
    exit 0
fi

for f in $1
do 
    ocrmypdf --image-dpi 300 $f ./output/$f.pdf
    echo "$f: Converted in output directory"
done

echo "Trying to consolidate all pages"

pdftk ./output/*.pdf cat output ./big-output.pdf

echo "Done"

