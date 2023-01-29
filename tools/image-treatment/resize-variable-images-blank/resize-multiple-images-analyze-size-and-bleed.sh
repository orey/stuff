#!/bin/bash

# Relations: height / width * 1000
A4=1414
USLETTER=1292

# Lulu default A4 210mm x 297mm bleed is 3mm top and bottom (6mm) and left and right (6mm), which corresponds to 2.9% width and 2.0% height
# Lulu default US Letter 216mm x 279mm bleed is 3.5mm top and bottom (7mm) and 3mm left and right (6mm), which corresponds to 2.8% width and 2.5% height
DEFAULT_BLEED_A4_WITH=29
DEFAULT_BLEED_A4_HEIGHT=20

DEFAULT_BLEED_US_WITH=28
DEFAULT_BLEED_US_HEIGHT=25

# Default values
DEFAULT_PERCENT=10


# usage
usage() {
    echo "This script will analyze all images in the folder in order to provide recommendations about the average size and the size with bleed margins."
    echo "$ ./resize-multiple-images-analyze-size-and-bleed.sh [pattern]"
    echo "Pattern must be separated by double quotes, such as \"*.ppm\""
    echo "Needs ImageMagick to be installed"
    exit 0
}

if [ $# != 1 ]
then
    usage
fi

REF=$A4
echo "In order to provide a good recommendation, please answer the questions."

read -p "Format? [a4,usletter] > " format
if [ $format = "a4" ] || [ $format = "A4" ]
then
    echo "Format: A4"
    format="a4"
else
    format="usletter"
    echo "Format: US Letter"
    REF=$USLETTER
fi

echo "Lulu default A4 210mm x 297mm bleed is 3mm top and bottom (6mm) and left and right (6mm), which corresponds to 2.9% width and 2.0% height"
echo "Lulu default US Letter 216mm x 279mm bleed is 3.5mm top and bottom (7mm) and 3mm left and right (6mm), which corresponds to 2.8% width and 2.5% height"
echo "You can choose default Lulu bleed ratio by inputing 0."
echo "Default value is $DEFAULT_PERCENT% (half on each side)"
read -p "Bleed percentage on fitting dimension? > " percent
if [ percent == 0 ]
then
    if [ $format = "a4"]
    then
        PERCENT_WIDTH=$DEFAULT_BLEED_A4_WITH
        PERCENT_HEIGHT=$DEFAULT_BLEED_A4_HEIGHT
    else
        PERCENT_WIDTH=$DEFAULT_BLEED_US_WITH
        PERCENT_HEIGHT=$DEFAULT_BLEED_US_HEIGHT
    fi
else
    re='^[0-9]+$'
    if ! [[ $percent =~ $re ]] ; then
        echo "Percentage is not a number. Keeping default $DEFAULT_PERCENT percent value."
        PERCENT_WIDTH=$DEFAULT_PERCENT
        PERCENT_HEIGHT=$DEFAULT_PERCENT
    else
        PERCENT_WIDTH=$percent
        PERCENT_HEIGHT=$percent
    fi
fi
echo "Bleed percentage taken: $PERCENT_WIDTH% width - $PERCENT_HEIGHT% height"

cumul_wi=0
cumul_he=0
count=0
for f in $1
do
    wi=$(identify -format "%w" "$f")
    he=$(identify -format "%h" "$f")
    cumul_wi=$(expr $cumul_wi + $wi)
    cumul_he=$(expr $cumul_he + $he)
    count=$(expr $count + 1)
    echo -n "$count|"
done
dim_wi=$(expr $cumul_wi / $count)
dim_he=$(expr $cumul_he / $count)
echo "Average dimension of images: $dim_wi x $dim_he"

# Calculate h/w
let rapport="1000 * $dim_he / $dim_wi"
echo "h/w = $rapport - to be compared with A4/US Letter relation being $A4/$USLETTER"
if [ $rapport -gt $REF ]
then
    echo "The width must be extended to be in $format format"
    let new_wi="1000 * $dim_he / $REF"
    echo "Width must be $new_wi to be in $format format: $new_wi x $dim_he"
    # The margin that counts is top and bottem margin in pixels
    let margin_he="$PERCENT_HEIGHT * $dim_he / 100"
    let size_he="$margin_he + $dim_he"
    let size_wi="1000 * $size_he / $REF"
    echo "Target size with $PERCENT_HEIGHT% margins top and bottom: $size_wi x $size_he"
    echo "Recommendation:"
    echo "Execute: ./resize-variable-images-blank3.sh \"$1\" $size_wi $size_he $new_wi $dim_he"
else
    echo "The height must be extended to be in $format format"
    let new_he="$REF * $dim_wi / 1000"
    echo "Height must be $new_he to be in $format format: $dim_wi x $new_he"
    # The margin that counts is left and right margin in pixels
    let margin_wi="$PERCENT_WIDTH * $dim_wi / 100"
    let size_wi="$margin_wi + $dim_wi"
    let size_he="$REF * $size_wi / 1000"
    echo "Target size with $PERCENT_WIDTH% margins left and right: $size_wi x $size_he"
    echo "Recommendation:"
    echo "Execute: ./resize-variable-images-blank3.sh \"$1\" $size_wi $size_he $dim_wi $new_he"
fi


