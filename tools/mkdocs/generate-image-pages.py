#---------------------------------------
# generate-image-pages.py
# Author: O. Rey
# Date: August 2020
# Licence: GPL V3
#---------------------------------------
#!/bin/python3
import os



def get_valid_folder(mystr):
    repindir = false
    while (not repindir):
        indir = input(mystr)
        if os.path.isdir(indir):
            return indir
        else:
            print("Folder is not valid.")

if __name__ == "__main__":
    indir = get_valid_folder("Input an image folder to analyze (sample: c:/sample/stuff): ")
    outdir = get_valid_folder("Input an output folder: ")


    
