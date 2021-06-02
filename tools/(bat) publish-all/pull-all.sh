#!/bin/bash
clear

echo Pulls all repos in this folder
echo Usage : pull-all.sh

read -p "Press any key to continue..."

for f in $(find . -maxdepth 1 -type d)
do
    echo -----------------------
    if [ $f == "." ]
    then
        echo . found, skipping...
    else
        echo $f
        cd $f
        git pull
        cd ..
    fi
done

echo "Done"

