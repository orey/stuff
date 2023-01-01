#!/bin/sh

clear

if [ $# != 1 ]
then
    echo "embed-fonts.sh: Script version 1"
    echo "Install gs first"
    echo "Usage : embedfont.sh [file.pdf]"
    exit 0
fi

new=embed-$1

pdffonts $1

read "Pausing. Type any key to continue..."


#gs -q -dNOPAUSE -dBATCH -dPDFSETTINGS=/prepress -sDEVICE=pdfwrite -sOutputFile=$new $1

# The list of fonts in teh system is here: /etc/fonts/fonts.conf

gs \
  -sFONTPATH=/usr/share/fonts:/usr/local/share/fonts:~/.local/share/fonts \
  -o $new \
  -sDEVICE=pdfwrite \
  -dPDFSETTINGS=/prepress \
   $1

echo "$new file generated"

pdffonts $new
