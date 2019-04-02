#---------------------------------------
# Screen capture Rafale
# Author: O. Rey
# Date: April 2019
# Licence: GPL V3
#---------------------------------------
# Usage: Change the TARGET directory right
# into this file. Images will be captured in
# a subdirectory.
# Features: Captures the images and generates
# a link that is copied in the clipboard
#---------------------------------------
#!/bin/python3

from mss import mss
from datetime import datetime
import os, sys, pyperclip
# import clipboard

from pathlib import Path

TARGET = 'C:/Path/To/__Screens'
NAME   = "default.png"

def format_link_md(completefilename):
    return "![screenshot](" + completefilename + ")"

def format_link_zim(completefilename):
    return "{{file:///" + completefilename.replace('\\', '/') + "}}"

if __name__ == "__main__":
    folder = input ("== Screen capture Rafale ==\nProvide a folder: ")
    if folder == "":
        folder = "default"
    targetdir = os.path.join(TARGET, folder)
    if not os.path.isdir(targetdir):
        os.makedirs(targetdir)
    image = ""
    shotnumber = 0
    devicenumber = 1
    outputformat = 0 # zim
    q = input("Device? [1] ")
    if q == "2":
        devicenumber = 2
    form = input("Format (zim or md)? [zim] ")
    if form == "md":
        outputformat = 1
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

        # Strange behavior on Windows: backslash is introduced
        # completefilename = os.path.join(targetdir, newfilename)

        completefilename = targetdir + '/' + newfilename
        os.rename(os.path.join(os.getcwd(),image), completefilename)
        print("Generated file: " + completefilename)
        if outputformat == 1:
            pyperclip.copy(format_link_md(completefilename))
            print("Filename copied to clipboard (md format)")
        else: 
            pyperclip.copy(format_link_zim(completefilename))
            print("Filename copied to clipboard (zim format)")
        
    
