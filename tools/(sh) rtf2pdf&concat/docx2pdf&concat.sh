#/bin/bash

for filename in ./*.docx
do
    libreoffice --headless --invisible --norestore --convert-to pdf "$filename"
done;

qpdf --empty --pages *.pdf -- allConcatenated.pdf

