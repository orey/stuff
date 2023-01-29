#!/bin/bash
clear

if [ $# != 2 ]
then
    echo "remove-page.sh: Script version 1"
    echo "Install pdftk first"
    echo "Usage : remove-page.sh [file.pdf] [page-number]"
    exit 0
fi

n=`pdfinfo $1 | grep Pages | awk '{print $2}'`
echo "The document has $n pages"

if [ $2 == 1 ]
then
    echo "Removing first page"
    pdftk A="$1" cat A2-$n output _hkztemp1.pdf
    mv _hkztemp1.pdf "$1"
    echo "Done"
    exit 0
fi

if [ $2 == $n ]
then
    echo "Removing last page"
    l=`expr $n - 1`
    pdftk A="$1" cat A1-$l output _hkztemp1.pdf
    mv _hkztemp1.pdf "$1"
    echo "Done"
    exit 0
fi

echo "Removing page $2 in the middle of the document"
i=`expr $2 - 1`
pdftk A="$1" cat A1-$i output _hkztemp1.pdf
j=`expr $2 + 1`
pdftk A="$1" cat A$j-$n output _hkztemp2.pdf

pdftk _hkztemp1.pdf _hkztemp2.pdf cat output $1
rm _hkztemp1.pdf
rm _hkztemp2.pdf

echo "Done"

