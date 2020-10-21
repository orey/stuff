#!/bin/sh
clear

if [ $# != 3 ]
then
    echo "concat-pdf-files.sh: Script version 1"
    echo "Install pdftk first"
    echo "Usage : concat-pdf-files.sh [file1.pdf] [file2.pdf] [outputfilename.pdf]"
    exit 0
fi

pdftk $1 $2 cat output $3

echo "Done"

