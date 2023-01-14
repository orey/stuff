import sys
import cv2
import numpy as np

def remove_dots(source, targetdir):
    img = cv2.imread(source, 0)
    _, blackAndWhite = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(blackAndWhite, None, None, None, 8, cv2.CV_32S)
    sizes = stats[1:, -1] #get CC_STAT_AREA component
    img2 = np.zeros((labels.shape), np.uint8)

    for i in range(0, nlabels - 1):
        if sizes[i] >= 50:   #filter small dotted regions
            img2[labels == i + 1] = 255

    res = cv2.bitwise_not(img2)
    cv2.imwrite('./' + targetdir + '/' + source, res)

def usage():
    print("Remove dots in scanned image")
    print("Usage:")
    print("> remove-dots.py [imagename] [location_folder]")
    print("location folder can be 'output'")

if __name__ ==  "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit(0)
    source = sys.argv[1]
    targetdir = sys.argv[2]
    remove_dots(source, targetdir)
    sys.exit(1)
    
    
            

    
            
