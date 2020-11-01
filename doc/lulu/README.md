# README

THis page provides some tricks about [lulu](https://www.lulul.com) publishing.

## Context of PDF with images

Printing PDFs with scanned images inside is not so easy in lulu.

### 1. Doc preparation with blank pages

Prepare the various elements of the document, while reminding there may be some blank pages in it.

For this, you can use the tool in the `insert-blank-page-in-pdf` folder (in tools).

### 2. Normalize your pages in A4 format and add print margin

For that purpose, you can use the `normalize-document-a4` tool.

More tricky stuff : you can have a look at the  `treat-pdf-with-image-files` tool which proposes more advanced uses of ImageMagick (convert).

### 3. Upload the document

Upload it on Lulu.

### 4. Compose your own cover

Download the Lulu template. Warning, the template will be exactly tuned for your pages so be sure your document will render weel before starting this step.

Extract Lulu template using `pdfimages`:

```
$ pdfimages lulu-template.pdf prefix
```

This will create an image name `prefix-000` that you will be able to edit with Gimp.

Upload your work on lulu and you're done.

## Classic series of actions for PDF with scans

* Use `pdfimages source.pdf` to extract bmp images from source.
* Find the proper geometry to resize all images at the same size, using `resize-images-fit.sh`.
* When all images are at the same format, create images with the proper ratio: `width / height = 0.707` in A4/A5. Compare with the artio of your images and add blank or black margins using `resize-images-blank.sh` or `resize-images-black.sh`.
* When you have the proper ratio, convert the bmp images into a compressed version with `convert-images.sh`. PNG is a good format.
* Generate a first version of your PDF by typing `convert *.pdf output1.pdf`. This can be very long if your book is big.
* Normalize your PDF with internal margins in A4 or A5 format with `normalize-document-a4.sh` or `normalize-document-a5.sh`.
* You can upload on Lulu.com.
