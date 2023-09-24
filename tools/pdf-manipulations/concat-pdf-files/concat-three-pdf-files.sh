#!/bin/sh
clear

if [ $# != 4 ]
then
    echo "concat-pdf-files.sh: Script version 1"
    echo "Install pdftk first"
    echo "Usage : concat-pdf-files.sh [file1.pdf] [file2.pdf] [file3.pdf] [outputfilename.pdf]"
    exit 0
fi

pdftk $1 $2 $3 cat output $4

echo "Done"

