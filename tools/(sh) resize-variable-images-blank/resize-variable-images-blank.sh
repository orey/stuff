#!/bin/bash
clear


# Define global variables
LOG="./exec.log"
ERROR_MARGIN=5 # Percentage of error for image size


# ensure_folder function enables to ensure that a target folder is existing
ensure_folder () {
    if [ ! -d ./$1 ]
    then
        mkdir ./$1
    else
        rm -R ./$1
        mkdir ./$1
    fi
}


# Create folders
ensure_folder vib
ensure_folder skipped


# Remove log file if exists
if [ -a $LOG]
then
    rm $LOG
fi


# Usage function
usage () {
    echo "resize-variable-images-blank.sh: Add margins to variable size images in order to reach a fixed image format"
    echo "---"
    echo "Usage : resize-images-blank.sh [pattern] [target-width] [target-height] [average-image-width] [average-image-height]"
    echo "1. Sample of pattern (put double quotes around it): *.JPG, myimages*.png"
    echo "2. All images will be centered into a target-width x target-height image"
    echo "3. If average-image-width and average image-height are provided, the script automatically resize to those value any image that would be too big."
    echo "   In case they are not provided, the image is skipped and copied to the 'skipped' directory."
    echo "Note: The script creates a 'vib' output directory (Variable Images Blank) with all converted images in it"
    echo "Requires: Imagemagick (identify, convert) to be installed"
}


# Analyzing number of parameters
if [ $# != 3 ] && [ $# != 5 ]
then
    usage
    exit 0
fi


# skipmode=true won't convert oversized images
skipmode=true
if [ $# == 5 ]
then
    skipmode=false
fi
echo "Info: skipmode = $skipmode"


# function to analyze the size of the image compared to the average size provided
# $1 file name
# $2 target width
# $3 target height
# The image is converted into "conv-s1" filename
analyze_image() {
    wi=$(identify -format "%w" "$1") 
    he=$(identify -format "%h" "$1")
    let "percentwi = 100 * ($wi - $2) / $2"
    let "percenthe = 100 * ($he - $3) / $3"
    if [ $percentwi -gt $ERROR_MARGIN ] || [ $percenthe -gt $ERROR_MARGIN ]
    then
        echo "[Analysis] Image $1 is out of the average range of image size"
    fi
}


# function to convert to the average size
# $1 file name
# $2 target width
# $3 target height
# The image is converted into "conv-s1" filename
convert_to_average () {
    convert $1 -resize $2x$3! conv-$1
}


# main loop on files
for f in $1
do
    skip=false
    toconvert=$f
    change=false
    # get image size
    width=$(identify -format "%w" "$f")
    height=$(identify -format "%h" "$f")
    echo "Converting image $f with size $width x $height"

    # margin width
    mw=$(expr $(expr $2 - $width) / 2 )
    echo "Margin width = $mw"

    # margin height
    mh=$(expr $(expr $3 - $height) / 2 )
    echo "Margin height = $mh"

    # Dealing with outsized images
    if [ $mw -lt 0 ] || [ $mh -lt 0 ]
    then
        if [ $skipmode == true ]
        then
            echo "Problem with image $f: height too big, please resize before applying margins"
            cp $f ./skipped
            skip=true
        else
            echo "--- $f image too big for target size, converting to average size first"
            convert_to_average $f $4 $5
            toconvert=conv-$f
            echo "--- $f was converted into $toconvert"
            echo "--- $f ($width x $ height) was converted into $toconvert ($4 x $5)" >> $LOG
            change=true
            # Need to recalculate the margins for the new image converted to the format $4 x $5
            mw=$(expr $(expr $2 - $4) / 2 )
            mh=$(expr $(expr $3 - $5) / 2 )
            echo "--- New margins for $toconvert: $mv, $mh"
        fi
    fi

    if [ $skip == false ]
    then
        echo "Adding margins to the image $toconvert"
        convert $toconvert -bordercolor white -border "$mw"x"$mh" ./vib/$f
        echo "$toconvert: Converted in output directory"
        echo "Borders added to $toconvert: Converted in output directory" >> $LOG
        # removing temporary file
        if [ $change == true ]
        then
          rm $toconvert
        fi
    fi
done

