#!/bin/bash

if [ $# != 2 ]
then
    echo "check-filename-size.sh: Script version 1"
    echo "Counts the number of characters of files with extension"
    echo "Usage : check-filename-size.sh \"[pattern]\" [size]"
    exit 0
fi

pattern=$1
size=$2

for f in $pattern
do
    s=${#f}
    if [ $s -ne $size ]
    then
        echo "Wrong size for file: " $f " - Size=" $s
    fi
done

echo "Done"
