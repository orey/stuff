#/bin/bash

for filename in ./*.rtf
do
    libreoffice --headless --invisible --norestore --convert-to pdf "$filename"
done;

qpdf --empty --pages *.pdf -- SRD-3-5.pdf

