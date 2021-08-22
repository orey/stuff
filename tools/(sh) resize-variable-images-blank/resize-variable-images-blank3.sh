#----------------------------------------
# Author: O. Rey rey.olivier@gmail.com
# Version: 3
# Licence: GPL v3
#----------------------------------------
#!/bin/bash
clear


PREFIX=$(date +"%Y%m%d_%H%M%S_")

# Define global variables
OUTPUT_FOLDER=$PREFIX
OUTPUT_FOLDER=+vib

# Generate log file name
LOG=$PREFIX
LOG+=resize-multiple.log

ERROR_MARGIN=5 # Percentage of error for image size
RESIZE=1
DONOTHING=0


# util
pause () {
    read -p "Press any key to continue..."
}


# ensure_folder function enables to ensure that a target folder is existing
ensure_folder () {
    if [ ! -d ./$1 ]
    then
        mkdir ./$1
#    else
#        rm -R ./$1
#        mkdir ./$1
    fi
}


# Create folder
ensure_folder $OUTPUT_FOLDER


# Remove log file if exists
if [ -a $LOG ]
then
    rm $LOG
fi


# Usage function
usage () {
    echo "resize-variable-images-blank3.sh: Add margins to variable size images in order to reach a fixed image format"
    echo "---"
    echo "Usage: resize-images-blank3.sh [pattern] [target-width] [target-height] [average-image-width] [average-image-height]"
    echo "--- The script resizes every image that is not in the format 'average-image-width' x 'average-image-height' with a $ERROR_MARGIN % of error"
    echo "1. Sample of pattern (put double quotes around it): *.JPG, myimages*.png"
    echo "2. All images will be centered into a target-width x target-height image (with blank margins around)"
    echo "Note: The script creates a 'vib' output directory (Variable Images Blank) with all converted images in it"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Get recommendations with the 'resize-multiple-image-analyze-size-and-bleed.sh' complementary script"
}


# function to analyze the size of the image compared to the average size provided
# $1 file name
# $2 average image width
# $3 average image height
# $4 mode: mode=1 => analyse seule; mode=2 => décision pour conversion
# returns: "1" if image must be resized to average and "0" if not
analyze_image() {
    wi=$(identify -format "%w" "$1") 
    he=$(identify -format "%h" "$1")
    let "temp1 = 100 * ($wi - $2) / $2"
    let "temp2 = 100 * ($he - $3) / $3"
    percentwi=${temp1#-}
    percenthe=${temp2#-}
    if [ $percentwi -gt $ERROR_MARGIN ] || [ $percenthe -gt $ERROR_MARGIN ]
    then
        if [ $4 == 1 ]
        then
            echo "[Analysis] Image $1 is out of the average range of image size: $wi x $he"
            echo "[Analysis] Image $1 is out of the average range of image size: $wi x $he" >> $LOG
        fi
        return $RESIZE
    else
        if [ $4 == 1 ]
        then
            echo "[Analysis] Image $1 ok"
            echo "[Analysis] Image $1 ok" >> $LOG
        fi
        return $DONOTHING
    fi
}


# Test mode
if [ $# == 6 ] && [ $6 == "test" ]
then
    for f in $1
    do
        analyze_image $f $4 $5 1
    done
    echo "Analyze written in $LOG"
    exit 0
fi


# Analyzing number of parameters
if [ $# != 5 ]
then
    usage
    exit 0
fi


# function to convert to the average size
# $1 file name
# $2 target width
# $3 target height
# The image is converted into "conv-s1" filename
convert_to_average () {
    convert $1 -resize $2x$3! conv-$1
}


# function to add blank margins
# $1 file name
# $2 margin width
# $3 margin height
# $4 target filename
# The image is moved into 
add_margins_to_image () {
    convert $1 -bordercolor white -border "$2"x"$3" ./$OUTPUT_FOLDER/$4
}


# main loop on files
for f in $1
do
    marginstoadd=$f
    tempfile=0

    # analyze image
    analyze_image $f $4 $5 2
    action=$?
    if [ $action == $RESIZE ]
    then
        echo "$f is too big or too small: redimensioning"
        echo "$f is too big or too small: redimensioning" >> $LOG
        convert_to_average $f $4 $5
        marginstoadd=conv-$f
        tempfile=1
    fi

    # get image size
    width=$(identify -format "%w" "$marginstoadd")
    height=$(identify -format "%h" "$marginstoadd")
    # echo "Converting image $marginstoadd with size $width x $height"

    # margin width and margin height
    mw=$(expr $(expr $2 - $width) / 2 )
    mh=$(expr $(expr $3 - $height) / 2 )
    # echo "Margins [width, height] = [$mw, $mh]"

    add_margins_to_image $marginstoadd $mw $mh $f
    echo "Margins added to $marginstoadd. Moved in output directory"
    echo "Margins added to $marginstoadd. Moved in output directory" >> $LOG

    # removing temporary file
    if [ $tempfile == 1 ]
    then
        rm conv-$f
    fi
    
done

