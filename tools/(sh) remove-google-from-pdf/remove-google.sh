#!/bin/bash
clear

# Usage
if [ $# != 1 ]
then
    echo "remove-google.sh: Script version 1"
    echo "Dependencies: pdfimages, convert"
    echo "Usage : remove-google.sh [file1.pdf]"
    exit 0
fi

# Creating technical folders
if [ ! -d ./to_remove ] # make sure the directory /_converted exists
then
    mkdir ./to_remove
    echo Created 'to_remove' folder
fi

if [ ! -d ./good_images ] # make sure the directory /_converted exists
then
    mkdir ./good_images
    echo Created 'good_images' folder
fi

# Extracting images from source pdf
echo Extracting images from file
pdfimages -png $1 test
echo Done extracting images

echo Padding image name to 4 digit
for i in *.png
do
    length=${#i}
    # test-953.pbm
    # 012345678901
    # test-0953.pbm
    # 01234 5678901
    if [ $length -eq 12 ]
    then
        mv ./"$i" "${i:0:5}0${i:5}"
    fi
done


echo Moving bad images into 'to_remove' folder
j=0
for i in *.png
do
    echo Image $i
    if [ $j -eq 0 ]
    then
        mv $i ./to_remove
        ((j+=1))
    elif [ $j -eq 1 ]
    then
        mv $i ./to_remove
        ((j+=1))
    else
        j=0
    fi
done

echo Images moved

new="${1%.*}_cleaned.pdf"
echo Creating new PDF $new
convert *.png $new
echo $new file creating

echo Cleaning good image files
mv *.png ./good_images

echo Done

