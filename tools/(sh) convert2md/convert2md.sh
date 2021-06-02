#/bin/sh

if [ ! -d ./_converted ] # make sure the directory /_converted exists
then
   mkdir ./_converted
fi

for i in *.html
do
    name=$(echo "$i" | cut -f 1 -d '.')
    echo "Converting $i"
    pandoc "$i" -f html -t markdown -s -o "./_converted/$name.md"
done


