#!/bin/bash
clear

if [ $# -eq 0 ]
then
    echo Publish all script (to master branch)
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
        git add *
        git commit -a -m "$message"
        git push origin master
        cd ..
    fi
done

echo "Done"

