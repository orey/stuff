#!/bin/bash
clear

for f in *.ppm
do
    echo "Splitting $f"
    left="${f%.*}.png"
    convert -crop 50%x100% +repage $f $left
done

echo "Done"

