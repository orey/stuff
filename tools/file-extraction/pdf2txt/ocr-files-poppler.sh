#/bin/sh

# ne marche pas top

fold=_ocr_poppler

if [ ! -d ./$fold ] # make sure the directory /_converted exists
then
   mkdir ./$fold
fi

for i in *.pdf
do
    name=$(echo "$i" | cut -f 1 -d '.')
    echo "*** Step 1: Make a pdf with a layer of text on images - $i"
    ocrmypdf --redo-ocr "$i" "./$fold/$name-ocr.pdf"
    echo "*** Step 2: Extract all text with Poppler utils"
    pdftotext "./$fold/$name-ocr.pdf" "./$fold/$name-ocr.txt"
done

echo "Done"

