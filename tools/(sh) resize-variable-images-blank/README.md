# Resize variable images with blank margins

## Problem statement

Old PDFs are often composed by scanned images. If you try to reprint them, you may be bound to add margins for the printing.

The problem is that, in many cases, the scanned images don't have the exact same size after being extracted by `pdfimages`.

Those scripts propose to automate some stuff around the treatment of the images.

## Prerequisites

Imagemagick must be installed. Images are probably extracted from PDF with `pdfimage`.

## resize-variable-images-blank.sh

This script has two options:

* One with 3 parameters
* One with 5 parameters

In the first option, the script will resize add margins to all images by fittinh them in the center of an image of size `width_in_pixels x height_in_pixels`.

Sample of use:

```
$ resize-variable-images-blank.sh 1700 1800
```

If your images have approximately the same size, that will be good, but if you have in the batch images that are very small or very big, the result may be strange.

The second option takes 2 parameters more defining the size of an average image. In case one of the margin is negative, the image is skipped and put in a `skipped` folder.

This script is not satisfying because small images are not dealt with.

Sample of use:

```
$ resize-variable-images-blank.sh 1700 1800 1176 1662
```

## resize-variable-images-blank2.sh

This second script is more consistent and more powerful. The 5 parameters are mandatory: pattern, size of the images with margin, size of the average image.

For each image, the script will analyze if its size differs from more than x% from the average image size. If it does, the script will resize the image to the average size, the image being bigger or smaller.

Sample of use:

```
$ resize-variable-images-blank2.sh 1700 1800 1176 1662
$ resize-variable-images-blank2.sh 1700 1800 1176 1662 test
```

Activate test mode with a 6th parameter to see how many images maybe converted in the process.


