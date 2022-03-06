#!/bin/sh
clear

if [ $# -eq 0 ]
then
    echo "mygrep script version 1 - insensitive to caps"
    echo "Usage : mygrep.sh \"pattern\""
    echo "Or usage: mygrep.sh folder \"pattern\""
    exit 0
fi

if [ $# -eq 1 ]
then
    grep -R -i $1 .
    exit 0
fi

if [ $# -eq 2 ]
then
    grep -R -i $2 ./$1
    exit 0
fi

echo "Try without arguments for help"


