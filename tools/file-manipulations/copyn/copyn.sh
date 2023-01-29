#!/bin/bash

clear

if [ ! -d ./_filtered ]		# make sure the directory /_converted exists
then
   mkdir ./_filtered
fi

rest=100

for i in {0..1000}
do
    count=$((i * 3))
    index=$((rest + count))
    istring=`printf %04d $index`
    filename=mo-$istring.pbm
    cp $filename ./_filtered
    #echo $filename
done

