#/bin/sh
clear

if [ $# != 1 ]
then
    echo "download-deb-in-webpage.sh: Script version 1"
    echo "Usage : ./download-deb-in-webpage.sh [URL]"
    exit 0
fi

echo "Downloading DEB"
wget -r -l 1 -nH -nd -np --ignore-case -A '*.deb' $1
echo "Done"

