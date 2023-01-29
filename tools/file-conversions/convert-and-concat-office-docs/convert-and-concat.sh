#Copyleft O. Rey 2018
#!/bin/bash

clear

if [ $# != 1 ]
then
  echo "convert-and-concat.sh: Script version 1 - convert a list of docx files into pdf and merge them into one big pdf"
  echo "You need LibreOffice and pdfunite installed to use this script"
  echo "Usage : convert-and-concat.sh [file-type]"
  exit 0
fi

echo "-------------------------------------------------------"
echo "--- 1. Convert each source file in pdf "
echo "-------------------------------------------------------"
for f in *.$1
do
  libreoffice --headless --convert-to pdf "$f"
done

echo "-------------------------------------------------------"
echo "--- 2. Creating _converted directory and move into it"
echo "-------------------------------------------------------"
if [ ! -d ./_converted ]		# make sure the directory /_converted exists
then
   mkdir ./_converted
fi

echo "-------------------------------------------------------"
echo "--- 3. Merge pdf  "
echo "-------------------------------------------------------"
pdfunite *.pdf ./_converted/merged-$1-documents.pdf

echo "-------------------------------------------------------"
echo "--- 4. Remove intermediate pdf files"
echo "-------------------------------------------------------"
rm *.pdf

echo "-------------------------------------------------------"
echo "--- Done  "
echo "-------------------------------------------------------"
