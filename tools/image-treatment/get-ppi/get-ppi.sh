#!/bin/sh
clear

if [ $# != 1 ]
then
    echo "get-ppi.sh: Script version 1"
    echo "Usage : get-ppi.sh filename"
    exit 0
fi

identify -units PixelsPerInch -format '%[fx:int(resolution.x)]\n' $1

