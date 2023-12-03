#/bin/sh
clear

if [ $# != 1 ]
then
    echo "download-pdf-in-webpage.sh: Script version 1"
    echo "Usage : ./download-pdf-in-webpage.sh [URL]"
    exit 0
fi

echo "Downloading PDF"
wget -r -l 1 -nH -nd -np --ignore-case -A '*.pdf' $1
echo "Downloading Images"
wget -r -l 1 -nH -nd -np --ignore-case -A '*.jpg' $1
wget -r -l 1 -nH -nd -np --ignore-case -A '*.png' $1
echo "Done"

