#!/bin/sh
clear

if [ ! -d ./converted ] # make sure the directory "converted" exists
then
   mkdir ./converted
fi

if [ $# != 2 ]
then
    echo "color-to-bw.sh: Script version 1"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : color-to-bw.sh [image_extension] [option]"
    echo "Option '1': pure black and white"
    echo "Option '2': grayscale"
    echo "Option '3': true grayscale (good)"
    echo "Other value: separate into grey channels"
    exit 0
fi

for f in *.$1
do
    if [ $2 -eq "1" ]
    then
        convert "$f" -monochrome ./converted/"$f"
    elif [ $2 -eq "2" ]
    then
         convert "$f" -remap pattern:gray50 ./converted/"$f"
    elif [ $2 -eq "3" ]
    then
        convert "$f" -colorspace Gray ./converted/"$f"
    else
        convert "$f" -separate ./converted/"$f"    
    fi
    echo "$f converted into ./converted/$f"
done

convert ./converted/*.$1 all.pdf

