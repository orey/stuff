#!/bin/bash
# A shell script to read file line by line

urlfilename="url.txt"
filename="liste.txt"

url=""

while read line
do
    # $line variable contains current line read from the file
    # display $line text on the screen or do something with it.
 
    echo "$line"
    url=$line
done < $urlfilename


while read line
do
    # $line variable contains current line read from the file
    # display $line text on the screen or do something with it.
 
    wget "$url$line"
done < $filename

