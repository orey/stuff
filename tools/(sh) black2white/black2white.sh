#!/bin/bash

if [ ! -d ./_converted ]		# make sure the directory /_converted exists
then
    mkdir ./_converted
fi

for f in *.pbm
do
    convert $f -negate ./_converted/$f
done

