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
$ resize-variable-images-blank.sh "*.ppm" 1700 1800
```

If your images have approximately the same size, that will be good, but if you have in the batch images that are very small or very big, the result may be strange.

The second option takes 2 parameters more defining the size of an average image. In case one of the margin is negative, the image is skipped and put in a `skipped` folder.

This script is not satisfying because small images are not dealt with.

Sample of use:

```
$ resize-variable-images-blank.sh "*.ppm" 1700 1800 1176 1662
```

## resize-variable-images-blank2.sh

### Standard use

This second script is more consistent and more powerful. The 5 parameters are mandatory: pattern, size of the images with margin, size of the average image.

For each image, the script will analyze if its size differs from more than x% from the average image size. If it does, the script will resize the image to the average size, the image being bigger or smaller.

Sample of use:

```
$ resize-variable-images-blank2.sh "*.ppm" 1700 1800 1176 1662
```

### Test use

```
$ resize-variable-images-blank2.sh "*.ppm" 1700 1800 1176 1662 test
```

Activate test mode with a 6th parameter to see how many images maybe converted in the process.

### Recommendation use

The recommendation mode is quite powerful because it will do all caculation for you.

```
$ resize-variable-images-blank2.sh "*.ppm" reco
```

Here is the list of actions that the script performs:

* It asks if the reference ratio is A4 or US Letter.
* It asks a bleed percentage to be applied on the fitting dimension (the one that is preserved to go to the target format).
* It browses all images and analyze their size to be able to calculate an average width and average height. If you have only a limit set of images that are totally out dimensions, please remove them for the analysis to get relevant figures.
    * This step will propose a recommendation for parameter 4 and 5 of the script (average width and height for redimensioning).
* It then analyzes the difference between the relation of height / width of the average page of the document and the target format (A4 or US Letter) and calculates the dimensions of the document with the margins.
* It then provides a full recommendation of script use.

Sample of use in A4:

```
In order to provide a good recommendation, please answer the questions.
Format? [a4,usletter]: a4
Format: A4
Bleed percentage on fitting dimension? 5
Bleed percentage chosen: 5%
1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|100|101|102|103|104|105|106|107|108|109|110|111|112|113|114|115|116|117|118|119|120|121|122|123|124|125|126|127|128|129|130|131|132|133|134|135|136|137|138|139|140|141|142|143|144|145|146|147|148|149|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167|168|169|170|171|172|173|174|175|176|177|178|179|180|181|182|183|184|185|186|187|188|189|190|191|192|193|194|195|196|197|198|199|200|201|202|203|204|205|206|207|208|209|210|211|212|213|214|215|216|217|218|219|220|221|222|223|224|225|226|227|228|229|230|231|232|233|234|235|236|237|238|239|240|241|Average dimension of images: 1165 x 1577
h/w = 1353 - to be compared with A4/US Letter relation being 1414/1292
The height must be extended to be in a4 format
Height must be 1647 to be in a4 format: 1165 x 1647
Target size with 5% margins left and right: 1281 x 1811
Recommendation:
Execute: ./resize-variable-images-blank2.sh "*.ppm" 1281 1811 1165 1647
```

Sample of use in US Letter:

```
In order to provide a good recommendation, please answer the questions.
Format? [a4,usletter]: usletter
Format: US Letter
Bleed percentage on fitting dimension? 5
Bleed percentage chosen: 5%
1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94|95|96|97|98|99|100|101|102|103|104|105|106|107|108|109|110|111|112|113|114|115|116|117|118|119|120|121|122|123|124|125|126|127|128|129|130|131|132|133|134|135|136|137|138|139|140|141|142|143|144|145|146|147|148|149|150|151|152|153|154|155|156|157|158|159|160|161|162|163|164|165|166|167|168|169|170|171|172|173|174|175|176|177|178|179|180|181|182|183|184|185|186|187|188|189|190|191|192|193|194|195|196|197|198|199|200|201|202|203|204|205|206|207|208|209|210|211|212|213|214|215|216|217|218|219|220|221|222|223|224|225|226|227|228|229|230|231|232|233|234|235|236|237|238|239|240|241|Average dimension of images: 1165 x 1577
h/w = 1353 - to be compared with A4/US Letter relation being 1414/1292
The width must be extended to be in usletter format
Width must be 1220 to be in usletter format: 1220 x 1577
Target size with 5% margins top and bottom: 1342 x 1734
Recommendation:
Execute: ./resize-variable-images-blank2.sh "*.ppm" 1342 1734 1220 1577
```

Note that the same document is analyzed in both cases, but with a different target:

* In the first case, we want to know what are the parameters to have a 5% bleed marging on a A4 document.
   * In that case, the height must be extended to reach an A4 format.
   * That means that the fitting dimension that will support the margin is the width.
* In the second case, the same of a US Letter document.
   * In that case, the width must be extended to reach a US Letter format.
   * That means that the fitting dimension that will support the margin is the height.
   
## resize-variable-images-blank3.sh

This script only proposes the `test` option. The recommendation option moved to a secondary script (`resize-multiple-images-analyze-size-and-bleed.sh`) containing the [Lulu](https://lulu.com) recommendations.

Please use the recommendation script, then resize your images using `resize-variable-images-blank3.sh`.

