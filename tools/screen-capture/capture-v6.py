#---------------------------------------
# Screen capture Rafale
# Author: O. Rey
# Date: January 2020
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

TARGET = 'C:/Users/a876246/Documents/oreyboulot-Airbus/Airbus Helicopters/__minutes/2020/'
NAME   = "default.png"

def format_link_md(completefilename):
    return "![screenshot](" + completefilename + ")"

def format_link_zim(completefilename):
    return "{{file:///" + completefilename.replace('\\', '/') + "?width=600}}"

def format_link_org(completefilename):
    return "[[file:" + completefilename.replace('\\', '/')+ "]]"

if __name__ == "__main__":
    folder = input ("== Screen capture Rafale ==\nProvide a folder (current month): ")
    if folder == "":
        folder = "default"
    targetdir = os.path.join(TARGET, folder)
    if not os.path.isdir(targetdir):
        os.makedirs(targetdir)
    image = ""
    shotnumber = 0
    devicenumber = 1
    outputformat = 2 # org
    q = input("Device? [1] ")
    if q == "2":
        devicenumber = 2
    meeting_name = input("Meeting name [meeting]:")
    if meeting_name == "":
        meeting_name = "meeting"
    form = input("Format (zim, md, org)? [org] ")
    if form == "md":
        outputformat = 1
    elif form == "zim":
        outputformat = 0
    all_links = []
    while True:
        q = input("Shot? [no] ")
        if q == "no":
            print("=> " + str(shotnumber) + " screenshots recorded in " + targetdir)
            mystr = ""
            for l in all_links:
                mystr = mystr + '\n' + l
            pyperclip.copy(mystr)
            print("=> All links of the session copied in the clipboard")
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
        newfilename = datetime.now().strftime("%Y%m%d_%H%M%S_%f") + '-' + meeting_name + ".png"

        # Strange behavior on Windows: backslash is introduced
        # completefilename = os.path.join(targetdir, newfilename)

        completefilename = targetdir + '/' + newfilename 
        os.rename(os.path.join(os.getcwd(),image), completefilename)
        print("Generated file: " + completefilename)
        if outputformat == 1:
            temp = format_link_md(completefilename)
            all_links.append(temp)
            pyperclip.copy(temp)
            print("Filename copied to clipboard (md format)")
        elif outputformat == 2:
            temp = format_link_org(completefilename)
            all_links.append(temp)
            pyperclip.copy(temp)
            print("Filename copied to clipboard (org format)")
        else:
            temp = format_link_zim(completefilename)
            all_links.append(temp)
            pyperclip.copy(temp)
            print("Filename copied to clipboard (zim format)")
        
    
