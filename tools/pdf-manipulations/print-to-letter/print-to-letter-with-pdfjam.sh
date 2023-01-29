#!/bin/bash
clear

if [ $# != 3 ]
then
    echo "print-to-letter.sh: Script version 1"
    echo "Install pdfjam first"
    echo "Usage : print-to-letter.sh [file.pdf] [scale] [suffix]"
    exit 0
fi

pdfjam --paper Letter --scale $2 --suffix "$3" -- $1

echo "Done"

