#!/bin/bash
clear

OUTPUT_DIR=pureBandW

# Generate log file name
KEY_LOG=pure-wb3-exec.log
LOG=$(date +"%Y%m%d_%H%M%S_")
LOG+=$KEY_LOG
$LOG


# Ensure directory function
ensure_directory () {
    if [ ! -d ./$1 ]
    then
        mkdir ./$1
    else
        rm -R ./$1
        mkdir ./$1
    fi
}

ensure pureBandW


# Usage function
usage () {
    echo "pure-bw.sh: Script version 1"
    echo "Set all images to pure black and white"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage: pure-bw [pattern] [black-grey-limit] [grey-white-limit] [option:forcegreylevel]"
    echo "Sample: pure-bw \"*.ppm\" 137 230"
    echo "Means between 0 and 136: black, between 137 and 229: nature grey, between 230 and 255: white"
    echo "If a 4th parameter is provided, the level of grey is imposed (not useful in most cases)."
    echo "Note: Patterns must be between double quotes"
    exit 0
}


# Analyze of number of parameters
if [ $# != 3 ] && [ $# != 4 ]
then
    usage
fi


# get grey level for the specific option of imposed grey
greylevel=0
if [ $# == 4 ]
then
    greylevel=$4
fi


# This function change a pixel of a certain color to another color
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
    if [ -e $1 ]
    then
        #filename + extension
        filename="${f%.*}"
        extension="${f#*.}"
        echo "File $f: [$filename,$extension]"
        cp $f old.$extension

        # Make pixels black
        echo -n "Black: "
        count=0
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

        # Write to log file
        echo "$f: Black, grey and white pixels treated" >> $LOG

        # move new file in output folder and clean temp file
        mv old.$extension ./pureBandW/$f
        rm temp.$extension
        echo "$f: done"
    else
        echo "$f file not existing. Probably a technical file. Skipping..."
    fi
done

