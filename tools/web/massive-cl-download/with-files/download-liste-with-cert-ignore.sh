#!/bin/bash

# Ce script gère les téléchargements massifs y compris pour des liens dans lesquels les accents
# français ont été replacés par des ?

clear

if [ $# != 2 ]
then
    echo "download-liste.sh: Script version 1"
    echo "Info: You need wget to run this script"
    echo "Usage : download-liste FILE-WITH-URL FILE-WITH-LIST"
    exit 0
fi

#urlfilename="url.txt"
#filename="liste2.txt"

urlfilename=$1
filename=$2

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
    echo "-------------------------------------------------"
    echo "Treating: $line"
    
    if [ -f "$line" ]; then
        echo "File already downloaded: $line"
        echo "Skipping..."
    else 
        echo "Downloading: $line"
        # ? must be translated into %3F
        line2=${line//"?"/%3F}
        line3=${line2//" "/%20}
        line4=${line3//"#"/%23}
        echo "Transformed: $line4"

        wget --no-check-certificate "$url$line4"

    fi
done < $filename

