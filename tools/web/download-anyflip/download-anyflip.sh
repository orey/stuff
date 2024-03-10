for i in $(seq 1 162);
do
    wget https://online.anyflip.com/hourn/fxho/files/mobile/$i.jpg
    mv $i.jpg $(printf %03d $i).jpg
done
img2pdf *.jpg -o result.pdf

