# Black and white transformation

## Problem statement

In PDF where the page is the result of scanned images, it is current that the scan color scale is grey and leads to bad printing result (too clear).

Those tools propose different correction strategies based on the manipulation of grays.

## Prerequisites

* ImageMagick must be installed

Generally images are coming from the use of `pdfimage` on the PDF.

## pure-bw.sh

This script propose to replace a **range of grays** by black pixels. The script is basic and processes only `ppm` files, but it is very easy to adapt it to other file formats.

Sample of use:

```
$ ./pure-bw.sh 0 130
```

## pure-bw2.sh

This script is more brutal: It is taking a certain level of gray as being the limit between black and white. All pixels below this level will be black, and all above will be white.

This can be useful in special situations, but in many cases, the result is ugly.

```
$ ./pure-bw2.sh 130
```

## pure-bw3.sh

The strategy of this script is a bit more advanced: It takes 2 values of grey. Between 0 and the lower one, all will be black; Between the lower one and the upper one, all greys will be preserved; And abover the second threshold, all greys will be turned to white.

This is particularly useful:

* To darken the fonts;
* To make any trace due to page transparency disappear.

```
$ ./pure-bw3.sh 130 220
```

This script also proposes an option to force a certain gray between the lower and the upper threshold. This can result in ugly stuff but can be useful sometimes.

```
$ ./pure-bw3.sh 0 130 180
```

