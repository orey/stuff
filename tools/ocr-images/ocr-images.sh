#!/bin/sh

clear

if [ $# != 1 ]
then
    echo "ocr-images.sh: Script version 1"
    echo "Requires: 'cuneiform' to be installed"
    echo "Usage : ocr-images.sh [image-extension] "
    exit 0
fi

for f in *.$1
do 
    echo "Converting $f"
    new="${f%.*}.txt"
    cuneiform -f text -l fra -o $new $f || echo "\n---\nProblem in $f\n---\n" > $new
done

echo "Concatenating all text files in 'all.txt'"
cat *.txt > all.txt

echo "Done"
