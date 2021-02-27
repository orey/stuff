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
    newcun="${f%.*}.txt"
    newtess="${f%.*}"
    cuneiform -f text -l fra -o $newcun $f  || tesseract $f $newtess -l fra
done

echo "Concatenating all text files in 'all.txt'"
cat *.txt > all.txt

echo "Done"
