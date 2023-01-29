#!/bin/bash
clear

if [ $# != 1 ]
then
    echo "remove-first-page.sh: Script version 1"
    echo "Install pdftk first"
    echo "Usage : remove-first-page.sh [file.pdf]"
    exit 0
fi

temp="$1"
nbofpages=$(pdfinfo "$1" | grep -Po 'Pages:[[:space:]]+\K[[:digit:]]+')

pdftk A="$1" cat 2-$nbofpages output xsdfsdrfd.pdf

mv xsdfsdrfd.pdf $1

echo "Done"

