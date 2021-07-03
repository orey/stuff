#!/bin/sh
clear

if [ ! -d ./pureBandW ] # make sure the directory "output" exists
then
    mkdir ./pureBandW
else
    rm -R ./pureBandW
    mkdir ./pureBandW
fi

if [ $# != 2 ]
then
    echo "pure-bw.sh: Script version 1"
    echo "Set all images to pure black and white"
    echo "Requires: Imagemagick (identify, convert) to be installed"
    echo "Usage : pure-bw [lowergraylevel] [uppergraylevel]"
    echo "Sample: pure-bw 59 137"
    exit 0
fi

for f in *.ppm
do 
    # Blank should be added
    # convert $f -modulate 100,0,0 ./pureBandW/$f
    # convert $f -fuzz 3% -fill black -opaque "#585858" ./pureBandW/$f
    count=$1
    cp $f old.ppm
    while [ $count -lt $2 ]
    do
        echo "Level: $count"
        convert old.ppm -fill black -opaque "rgb($count,$count,$count)" new.ppm
        mv new.ppm old.ppm
        count=`expr $count + 1`
    done
    mv old.ppm ./pureBandW/$f
    echo "$f: done"
done

