#!/bin/bash

LOG=logfile.log

if [ $# != 1 ]
then
    echo "Usage:"
    echo "$ ./remove-bad-char-in-names.sh \"#\" "
    echo "Char must be between double quotes"
    echo "It is probable that many characters also works like \"#;_\". To be tested."
    exit 0
fi


find . -depth -name "*[$1]*" -print > temp.txt

count=0
while read line
do
    dir="${line%/*}"                 # Get the folder its inside
    filename="${line/*\/}"           # Get the plain name.
    new="${filename//$1/_}"          # Substitute _ for bad things.
    mv "$dir/$filename" "$dir/$new"  # Rename it.
    echo "Renamed: [$dir/$filename]"
    echo "   into: [$dir/$new]"
    echo "Renamed: [$dir/$filename]" >> $LOG
    echo "   into: [$dir/$new]" >> $LOG
    count=$(expr $count + 1)
done < temp.txt

rm temp.txt

echo "$count files renamed"

