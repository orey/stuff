#/bin/sh

fold=_ocr

if [ ! -d ./$fold ] # make sure the directory /_converted exists
then
   mkdir ./$fold
fi

for i in *.pdf
do
    name=$(echo "$i" | cut -f 1 -d '.')
    echo "Converting $i"
    # the previous ocrisation are quite bad
    ocrmypdf --force-ocr --sidecar "./$fold/$name.txt" "$i" "./$fold/$name.pdf"
done

echo "Done"

