#!/bin/sh

clear

if [ $# != 1 ]
then
    echo "ocr-images.sh: Script version 1"
    echo "Requires: 'cuneiform' AND 'tesseract' to be installed"
    echo "Setup for french"
    echo "Usage : ocr-images.sh [image-extension]"
    exit 0
fi

for f in *.$1
do 
    echo "Converting $f"
    new="${f%.*}.txt"
    cuneiform -f text -l fra -o $new $f  || tesseract $f $new -l fra
done

echo "Concatenating all text files in 'all.txt'"
cat *.txt > all.txt

echo "Done"
