#!/bin/bash
clear

if [ ! -d ./converted ] # make sure the directory "converted" exists
then
   mkdir ./converted
fi

if [ $# -eq 0 ]
then
    echo "rotate-multiple.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : rotate-multiple.sh [input.pdf] [page1] ... [pagen]"
    exit 0
fi

pdfimages $1 temp

# Le but est de trouver le nom de l'image à retourner
# décalage de 1 car pdfimages commence à 0 + padde à trois chiffres

for n in $@
do
    if [ $n = $1 ]
    then
        echo "skip"
    else    
        m=`expr $n - 1`
        s=`printf "%03d\n" $m`
        k="temp-$s.ppm"
        echo $k
        # anticlockwise
        convert $k -rotate 90 abc-$k
        mv abc-$k $k
    fi
done
convert temp-*.ppm new_$1
rm temp-*.ppm
echo "Done. Wrote: new_$1"




echo "Done"


