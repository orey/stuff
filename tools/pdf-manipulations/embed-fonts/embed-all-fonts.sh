#!/bin/bash
clear

if [ $# != 2 ]
then
    echo "embed-all-fonts.sh: Script version 1"
    echo "Install ghostscript first"
    echo "Usage : embed-all-fonts.sh [input.pdf] [output.pdf]"
    exit 0
fi

file_exist () {
    exists=false
    if [ -e "$1" ]; then
        echo "true"
    else
        echo "false"
    fi
}

ex="$(file_exist $1)"

if [ "$ex" == "false" ]; then
    echo "File $1 does not exist. Exiting..."
    exit 0
fi

gs -q -dNOPAUSE -dBATCH -dPDFSETTINGS=/prepress -sDEVICE=pdfwrite -sOutputFile=$2 $1

echo "$1 was processed into $2"

echo "Done"

