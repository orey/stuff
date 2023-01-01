# US Letter:  11 in x 8.5 in
#            279 mm x 216 mm
# 300dpi x 8.5 inch = 2550
# 300dpi x 11 inch  = 3300
convert $1 -density "300" -resize "2550x3300" resized-letter.pdf
