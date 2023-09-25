#----------------------------------------
# Author: O. Rey rey.olivier@gmail.com
# Version: 3
# Licence: GPL v3
# September 2023
#----------------------------------------
#!/bin/bash
clear

# count param number
if [ $# != 1 ]
then
    echo "Usage: ./analyze_images.sh [pattern]"
    echo "Sample of pattern (put double quotes around it): *.JPG, myimages*.png"
    exit 0
fi

for f in $1
do
    swi=$(identify -format "%w" "$f") 
    she=$(identify -format "%h" "$f")
    echo "$f: $swi x $she"
done

