#!/bin/bash
clear

for f in *.jpg
do
    echo "Splitting $f"
    left="split-${f%.*}.jpg"
    convert -crop 50%x100% +repage $f $left
done

echo "Done"

