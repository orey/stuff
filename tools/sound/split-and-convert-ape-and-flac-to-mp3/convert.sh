# Copyleft O. Rey 2012
#!/bin/bash

clear

if [ $# != 2 ]
then
  echo "convert.sh: Script version 2 - take in charge big ape or flac files"
  echo "Usage : convert.sh [name-of-cue-without-extension] [type]"
  echo "- type can be [ape] or [flac]"
  echo "Try not to use spaces in parameters"
  exit 0
fi

echo "-------------------------------------------------------"
echo "--- 1. Creating _converted directory and move into it"
echo "-------------------------------------------------------"
if [ ! -d ./_converted ]		# make sure the directory /_converted exists
then
   mkdir ./_converted
fi
cd ./_converted

echo "-------------------------------------------------------"
echo "--- 2. Cut APE with CUE + compression in flac"
echo "-------------------------------------------------------"
if [ $2 = "ape" ]
then
  extens="ape"
else
  extens="flac"
fi
if [ ! -r ../$1.$extens ]
then
  echo "Error: File not found"
  echo ../$1.$extens
  exit 0
fi
cuebreakpoints ../$1.cue | shnsplit -o flac ../$1.$extens
 
echo "-------------------------------------------------------"
echo "--- 3. Tag of flac files with CUE"
echo "-------------------------------------------------------"
cuetag ../$1.cue split-track*.flac
 
echo "-------------------------------------------------------"
echo "--- 4. Rename flac files with Tag (TRACKNUMBER - TITLE.flac)"
echo "-------------------------------------------------------"
for i in split-track*.flac
do
        titre=$(metaflac --show-tag=TITLE "$i")
        piste=$(metaflac --show-tag=TRACKNUMBER "$i")
        mv "$i" "${piste#TRACKNUMBER=} - ${titre#TITLE=}.flac"
done


echo "-------------------------------------------------------"
echo "--- 5. Convert flac in mp3"
echo "-------------------------------------------------------"
for i in *.flac
do
  flac -d -f "$i"
  rm "$i"
done

for i in *.wav
do
  new = basename 
  lame -V0 "$i" "$i.mp3"
  rm "$i"
done

echo "-------------------------------------------------------"
echo "--- 6. Rename"
echo "-------------------------------------------------------"
for f in *.mp3
  do mv "$f" "${f%wav.mp3}mp3"
done

echo "-------------------------------------------------------"
echo "--- 7. Go back to original directory"
echo "-------------------------------------------------------"
cd ..



