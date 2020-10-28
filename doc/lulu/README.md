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

