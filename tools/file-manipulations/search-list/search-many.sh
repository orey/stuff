#!/bin/bash

clear 

if [ $# -eq 0 ]
then
    echo "search-many.sh: Script version 1"
    echo "Usage : search-many [keyword1] [keyword2] ... [keywordn]"
    exit 0
fi

for keyword in "$@"; do
    echo "----------------------------------------"
    echo "Searching: $keyword"
    find . -iname "*$keyword*" -type f
done
