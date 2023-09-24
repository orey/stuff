#!/bin/bash
clear

if [ $# != 3 ]
then
    echo "rotate-page.sh: Script version 1"
    echo "Install pdftk first"
    echo "Usage : rotate-page.sh [file.pdf] [page-number] [1/2]"
    echo "1: rotate clockwise"
    echo "2: rotate counter clockwise"
    exit 0
fi

# Function that rotates a one page pdf  ($1:filename, $2:1/2 comme au dessus)
rotate_page () {
    if [ $2 == 1 ]
    then
        pdftk $1 cat 1-endright output _rotated1212.pdf
    else
        pdftk $1 cat 1-endleft output _rotated1212.pdf
    fi
    mv _rotated1212.pdf $1
}

# function to extract pages, takes 3 parameters
# filename, range, output
extract_pages () {
    pdftk A="$1" cat A$2 output $3
}

concat_two_files () {
    pdftk $1 $2 cat output $3
}

concat_three_files () {
    pdftk $1 $2 $3 cat output $4
}



n=`pdfinfo $1 | grep Pages | awk '{print $2}'`
echo "The document has $n pages"

if [ $2 == 1 ]
then
    echo "Rotating the first page"
    # extract first page then the rest
    extract_pages $1 1-1 _torotate1212.pdf
    extract_pages $1 2-$n _rest1212.pdf
    rotate_page _torotate1212.pdf $3
    concat_two_files _torotate1212.pdf _rest1212.pdf _output1212.pdf
    mv _output1212.pdf $1
    echo "Done"
    exit 0
fi

if [ $2 == $n ]
then
    echo "Rotating the last page"
    l=`expr $n - 1`
    # extract last page then rest
    extract_pages $1 $n-$n _torotate1212.pdf
    extract_pages $1 1-$l _rest1212.pdf
    rotate_page _torotate1212.pdf $3
    concat_two_files _rest1212.pdf _torotate1212.pdf _output1212.pdf
    mv _output1212.pdf $1
    echo "Done"
    exit 0
fi

echo "Rotating a page in the middle of the document"
l=`expr $2 - 1`
m=`expr $2 + 1`
extract_pages $1 $2-$2 _torotate1212.pdf
extract_pages $1 1-$l _before1212.pdf
extract_pages $1 $m-$n _after1212.pdf
rotate_page _torotate1212.pdf $3
concat_three_files _before1212.pdf _torotate1212.pdf _after1212.pdf _output1212.pdf
mv _output1212.pdf $1
echo "Done"
exit 0
