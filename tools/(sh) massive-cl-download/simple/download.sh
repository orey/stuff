#/bin/bash

clear

if [ $# != 2 ]
then
    echo "download.sh: Script version 1"
    echo "Info: You need wget to run this script"
    echo "Usage : download INF SUP"
    exit 0
fi

for i in $(seq -f "%03g" "$1" "$2")
do
    echo $i
    wget http://download.abandonware.org/magazines/Jeux%20et%20Strategie/jeuxetstrategie_numero$i.zip
done

echo "Done"

