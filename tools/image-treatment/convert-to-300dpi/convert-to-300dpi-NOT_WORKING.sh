#!/bin/sh
clear

if [ $# != 2 ]
then
    echo "convert-to-300dpi.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : convert-to-300dpi.sh [source-format] [target-format]"
    exit 0
fi

if [ ! -d ./300dpi ] # make sure the directory "converted" exists
then
   mkdir ./300dpi
fi

limit=16383
#limit=4000

# fonction avec 2 paramètres (à ne pas confondre avec les paramètres du script)
# $1 est le nom du fichier à convertir
# $2 est le format 
myConvert() {
    new="${1%.*}.$2"
    echo "Current resolution is:"
    identify -format '%x,%y\n' $1
    convert -units PixelsPerInch $1 -resample 300x300 ./300dpi/$new
    echo "$1 converted into ./300dpi/$new"
}

for f in *.$1
do
    w=`identify -format %w $f`
    h=`identify -format %h $f`
    echo "Size of image: width= $w / height= $h"
    if [ $w -gt $limit ] || [ $h -gt $limit ]
    then
        echo "Width or height is too big (superior to $limit). Resizing..."
        extension="${f##*.}"
        echo "File extension: $extension"
        newname="${f%.$extension}-resized.$extension"
        convert $f -resize $limit@ $newname
        myConvert $newname $2
    else
        myConvert $f $2
    fi
done
