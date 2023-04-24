#!/bin/bash

# Ce script gère les téléchargements massifs y compris pour des liens dans lesquels les accents
# français ont été replacés par des ?

clear

if [ $# != 1 ]
then
    echo "search-list.sh: Script version 1"
    echo "Usage : search-list [FILE-WITH-LIST]"
    echo "List is composed of a set of two lines:"
    echo "-The first one with the description"
    echo "-The second one with the keyword"
    exit 0
fi

listfile=$1
count=0
report=report.txt

while read line
do
    if [ $count -eq 0 ]; then
        echo "++++++++++++++++++++++++++++++++++++++++++++++++"
        echo "++++++++++++++++++++++++++++++++++++++++++++++++" >> $report
        # first line: description
        echo "$line"
        echo "$line" >> $report
        count=1
    else
        echo "Keywords provided: $line"
        echo "Keywords: $line" >> $report

        for keyword in $line; do
            echo "----------------------------------------"
            echo "----------------------------------------" >> $report
            echo "Searching: $keyword"
            echo "Searching: $keyword" >> $report
            find . -iname "*$keyword*" -type f
            find . -iname "*$keyword*" -type f >> $report
        done

        count=0
    fi
done < $listfile

echo "See generated report: $report"

