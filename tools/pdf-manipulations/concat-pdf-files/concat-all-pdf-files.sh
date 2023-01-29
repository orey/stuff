#!/bin/sh
clear

if [ $# != 1 ]
then
    echo "concat-all-pdf-files.sh: Script version 1"
    echo "Install pdftk first"
    echo "Usage : concat-all-pdf-files.sh [outputfilename.pdf]"
    exit 0
fi

pdftk *.pdf cat output $1

echo "Done"

