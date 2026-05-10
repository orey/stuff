# README

## French OCRization

For French OCR, don't forget the following:

```
root> apt install tesseract-ocr-fra
```

Then:

```
> ocrmypdf -l fra source.pdf target.pdf
```

## 2 useful options

```
> ocrmypdf --force-ocr --sidecar text.txt source.pdf target.pdf
```

* `--force-ocr` gets rid of the previous text layer and redo averything again
* `--sidecar` extract the text in a text file, quite useful for automated text manipulation

## 2 pages files

* `--tesseract-pagesegmode 1` 



