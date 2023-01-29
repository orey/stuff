#!/bin/bash
clear

if [ $# -eq 0 ]
then
    echo Publish all script by calling the publish script in each folder
    echo Usage : publish-all.sh [comments without space]
    exit 0
fi

message=$@

for f in $(find . -maxdepth 1 -type d)
do
    echo -----------------------
    if [ $f == "." ]
    then
        echo . found, skipping...
    else
        echo $f
        cd $f
        ./publish.sh "$message"
        cd ..
    fi
done

echo "Done"

