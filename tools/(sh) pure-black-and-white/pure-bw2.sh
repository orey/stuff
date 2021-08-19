#!/bin/bash
clear

if [ ! -d ./pureBandW ] # make sure the directory "output" exists
then
    mkdir ./pureBandW
else
    rm -R ./pureBandW
    mkdir ./pureBandW
fi

if [ $# != 2 ]
then
    echo "pure-bw.sh: Script version 1"
    echo "Set all images to pure black and white"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : pure-bw [pattern] [black-white-limit]"
    echo "Sample: pure-bw \"*.ppm\" 224"
    echo "Means > [224,224,224] will be white and black if inferior"
    echo "Patterns must be between double quotes"
    exit 0
fi

for f in $1
do 
    cp $f old.ppm
    echo -n "Black: "
    count=0
    # Make pixels black
    while [ $count -lt $2 ]
    do
        echo -n "$count|"
        convert old.ppm -fill black -opaque "rgb($count,$count,$count)" new.ppm
        mv new.ppm old.ppm
        count=$( expr $count + 1 )
    done

    # Make pixels white
    echo -n "White: "
    while [ $count -lt 255 ]
    do
        echo -n "$count|"
        convert old.ppm -fill white -opaque "rgb($count,$count,$count)" new.ppm
        mv new.ppm old.ppm
        count=$( expr $count + 1 )
    done

    # move new file in output folder
    mv old.ppm ./pureBandW/$f
    echo "$f: done"
done

