#!/bin/sh
clear

if [ $# != 2 ]
then
    echo "normalize-document-a4.sh: Script version 1"
    echo "Requires: pdfinfo and pdfjam to be installed"
    echo "Usage : normalize-document-a4.sh [in.pdf] [out.pdf]"
    exit 0
fi

pdfinfo $1

echo "Processing $1"
pdfjam --outfile $2 --paper a4paper $1

pdfinfo $2

echo "Done"


