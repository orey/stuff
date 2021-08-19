#!/bin/bash
clear

if [ ! -d ./pureBandW ] # make sure the directory "output" exists
then
    mkdir ./pureBandW
else
    rm -R ./pureBandW
    mkdir ./pureBandW
fi

if [ $# != 3 ] && [ $# != 4 ]
then
    echo "pure-bw.sh: Script version 1"
    echo "Set all images to pure black and white"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : pure-bw [pattern] [black-grey-limit] [grey-white-limit] [option:forcegreylevel]"
    echo "Sample: pure-bw \"*.ppm\" 137 230"
    echo "Means between 0 and 136: black, between 137 and 229: grey, between 230 and 255: white"
    echo "Patterns must be between double quotes"
    exit 0
fi


# get grey level
greylevel=0
if [ $# == 4 ]
then
    greylevel=$4
fi


# $1: image filename
# $2: source color
# $3: target color
# $4: target image
change_pixel_in_image () {
    convert $1 -fill $3 -opaque $2 $4
    mv $4 $1
}


# Main loop
for f in $1
do
    #filename + extension
    filename="${f%.*}"
    extension="${f#*.}"
    echo "File $f: [$filename,$extension]"
    cp $f old.$extension
    echo -n "Black: "
    count=0
    # Make pixels black
    while [ $count -lt $2 ]
    do
        echo -n "$count|"
        change_pixel_in_image old.$extension  "rgb($count,$count,$count)" "rgb(0,0,0)" temp.$extension
        count=$( expr $count + 1 )
    done

    # Make pixels grey or preserve existing grey
    if [ $greylevel != 0 ]
    then
        while [ $count -lt $3 ]
        do
            echo -n "$count|"
            change_pixel_in_image old.$extension "rgb($count,$count,$count)" "rgb($greylevel,$greylevel,$greylevel)" temp.$extension
            count=$( expr $count + 1 )
        done
    else
        count=$3
    fi

    # Make pixels white
    echo -n "White: "
    while [ $count -lt 255 ]
    do
        echo -n "$count|"
        change_pixel_in_image old.$extension  "rgb($count,$count,$count)" "rgb(255,255,255)" temp.$extension
        count=$( expr $count + 1 )
    done

    # move new file in output folder
    mv old.$extension ./pureBandW/$f
    echo "$f: done"
done

