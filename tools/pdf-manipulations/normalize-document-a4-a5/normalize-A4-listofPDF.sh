#!/bin/sh
clear

if [ ! -d ./_normalized ] # make sure the directory exists
then
   mkdir ./_normalized
fi

temp=temp_luhgqirue.pdf

for f in *.pdf
do
    pdfinfo $f
    echo "Processing $f"
    #pdfjam --outfile $temp --paper a4paper --scale 0.9 $f
    pdfjam --outfile $temp --paper a4paper $f
    mv $temp ./_normalized/$f
done

echo "Done"


