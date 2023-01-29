#/bin/bash
clear

if [ $# != 1 ]
then
    echo "process.sh: Script version 1"
    echo "Use :"
    echo "> ./process.sh [file.pdf]"
    exit 0
fi

file=$1
echo "$1"
myfile=${file%.*}
echo "$myfile"

echo "Get cover page"
pdfimages $1 a
convert a-000.ppm $myfile-cover.png
rm *.ppm
echo "Done"

read -p "Remove first page? " yn
case $yn in
    [yY]* ) ./remove-first-page.sh $1;;
    * ) echo "No first page removal";;
esac

echo "Print to real US Letter"
# En 0.95 ça marche bien aussi
pdfjam --paper Letter --scale 1.0 --suffix 'letter' -- $1
#lp -d PDF -o media=Letter -o fit-to-page $1
echo "Done"
# le nom du fichier est maintenant $myfile-letter.pdf

echo "Flatten PDF"
echo "$myfile-letter.pdf $myfile-letter-flattened.pdf"
pdf2ps "$myfile-letter.pdf" toto.ps
ps2pdf toto.ps "$myfile-letter-flattened.pdf"
rm toto.ps
echo "Done"

read -p "Insert a blank page in $myfile-letter-flattened.pdf? If yes type page number, else 0: " n
case $n in
    [0]* )  exit 0; break;;
    [1-9]* ) ./insert-blank-page-letter-at.sh $n $myfile-letter-flattened.pdf $myfile-letter-flatenned-with-BP.pdf;;
    * ) exit 0;;
esac


