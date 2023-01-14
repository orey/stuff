#!/bin/bash
for i in *.wav
do
    ffmpeg -i "$i" -ab 320k -f mp3 "${i%}.mp3"
done
