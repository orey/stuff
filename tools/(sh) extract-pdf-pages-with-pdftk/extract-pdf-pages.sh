#!/bin/bash
clear

if [ $# != 3 ]
then
    echo "extract-pdf-pages.sh: Script version 1"
    echo "Install pdftk first"
    echo "Usage : extract-pdf-pages.sh [file.pdf] [range] [outputfilename]"
    echo "- range must be numbers separated by dash (sample 10-22)"
    exit 0
fi

pdftk A="$1" cat A$2 output $3

echo $1

echo "Done"

