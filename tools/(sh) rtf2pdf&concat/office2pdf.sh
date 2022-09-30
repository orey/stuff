#/bin/bash

echo "------------------------"
echo "Transforming docx to pdf"
for filename in ./*.docx
do
    echo $filename
    libreoffice --headless --invisible --norestore --convert-to pdf "$filename"
done;

echo "------------------------"
echo "Transforming doc to pdf"
for filename in ./*.doc
do
    echo $filename
    libreoffice --headless --invisible --norestore --convert-to pdf "$filename"
done;

echo "------------------------"
echo "Transforming pptx to pdf"
for filename in ./*.pptx
do
    echo $filename
    libreoffice --headless --invisible --norestore --convert-to pdf "$filename"
done;

echo "------------------------"
echo "Transforming ppt to pdf"
for filename in ./*.ppt
do
    echo $filename
    libreoffice --headless --invisible --norestore --convert-to pdf "$filename"
done;

echo "Done"
