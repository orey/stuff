#!/bin/bash
clear

if [ $# -eq 0 ]
then
    echo "split-multiple.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : split-multiple.sh [input.pdf] [page1] ... [pagen]"
    exit 0
fi

pdfimages $1 temp

# Le but est de trouver le nom de l'image à retourner
# décalage de 1 car pdfimages commence à 0 + padde à trois chiffres

for n in $@
do
    if [ $n = $1 ]
    then
        echo "Working..."
    else    
        m=`expr $n - 1`
        s=`printf "%03d\n" $m`
        k="temp-$s.ppm"
        echo $k
        cp $k ./converted/$k
        # Find the size of the image
        w=`identify -format %w $k`
        h=`identify -format %h $k`

        # C'est bizarre, je pensais que le tests était dans l'autre sens
        if [ $h < $w ]
        then
            echo "Image verticale"
            newh=`expr $h / 2`
            echo "Après division : $newh"
            # convert dec in int
            #newh1=`printf "%.*f\n" 0 "$newh"`
            #neww1=${neww%.*}
            newh1=$newh
            echo "Rounded : $newh1"
            newh2=`expr $h - $newh1`
            leftpage="${k%.*}a.ppm"
            rightpage="${k%.*}b.ppm"
            
            convert $k -crop ${w}x${newh1}+0+0 +repage $leftpage
            convert $k -crop ${w}x${newh2}+0+${newh1} +repage $rightpage
        else
            echo "Image horizontale"
            neww=`expr $w / 2`
            echo "Après division : $neww"
            # convert dec in int
            neww1=`printf "%.*f\n" 0 "$neww"`
            #neww1=${neww%.*}
            neww1=$neww
            echo "Rounded : $neww1"
            neww2=`expr $w - $neww1`
            leftpage="${k%.*}a.ppm"
            rightpage="${k%.*}b.ppm"
            
            convert $k -crop ${neww1}x${h}+0+0 +repage $leftpage
            convert $k -crop ${neww2}x${h}+${neww1}+0 +repage $rightpage
        fi
        rm $k
    fi
done

for f in *.ppm
do
    convert $f "${f%.*}.jpg"
done
convert *.jpg new_$1
rm temp-*.ppm
rm temp-*.jpg
echo "Done. Wrote: new_$1"


