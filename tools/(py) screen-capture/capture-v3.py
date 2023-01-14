#---------------------------------------------------------
# Script to automate the screenshots
# Author: O. Rey
# License: GPL V3
# Version: 3
# Date: March 20 2019
#---------------------------------------------------------
#!/bin/python3

from mss import mss
from datetime import datetime
import os, sys, pyperclip
# import clipboard

from pathlib import Path

TARGET = 'C:/path/to/note/folder'
NAME   = "default.png"

if __name__ == "__main__":
    print("== Screen Capture Rafale == ")
    targetdir = TARGET
    if not os.path.isdir(targetdir):
        os.makedirs(targetdir)
    image = ""
    shotnumber = 0
    devicenumber = 1
    q = input("Device? [1] ")
    if q == "2":
        devicenumber = 2
    while True:
        q = input("Shot? [no] ")
        if q == "no":
            print("=> " + str(shotnumber) + " screenshots recorded in " + targetdir)
            print("Bye")
            s = input("Type any key to exit")
            exit(1)
        with mss() as sct:
            image = sct.shot(mon=devicenumber)
            shotnumber += 1
            print("Shot done")
        if image == "":
            print("Capture failed. Exiting.")
            exit(0)
        newfilename = datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".png"
        os.rename(os.path.join(os.getcwd(),image), os.path.join(targetdir, newfilename))
        print("Generated file: " + newfilename)
        pyperclip.copy("![screenshot](" + newfilename + ")")
        print("Filename copied to clipboard (MD link format)")
        
    
