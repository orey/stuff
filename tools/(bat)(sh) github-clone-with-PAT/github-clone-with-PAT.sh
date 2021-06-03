#!/bin/bash
clear

if [ $# != 1 ]
then
    echo Github clone script using PAT
    echo Usage : clone-github.sh [name_of_repo]
    exit 0
fi

pat=`cat ./PAT.txt`
git clone https://orey:$pat@github.com/orey/$1.git

echo Done

