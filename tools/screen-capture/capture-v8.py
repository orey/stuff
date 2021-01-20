#---------------------------------------
# Screen capture Rafale
# Author: O. Rey
# Date: January 2020 updated Jan 21
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
import cv2

from pathlib import Path

TARGET = 'C:/path/to/images/'
NAME   = "default.png"

FORMAT_ZIM = 0
FORMAT_ORG = 1
FORMAT_MD  = 2

THUMBNAIL_PERCENT = 10

#------------------------------------------------
# Resize image
#------------------------------------------------
def resize_image(path, imagename):
    image = cv2.imread(path + '/' + imagename)
    width = int(image.shape[1] * THUMBNAIL_PERCENT / 100)
    height = int(image.shape[0] * THUMBNAIL_PERCENT / 100)
    dim = (width, height)
    # resize image
    #resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    resize = cv2.resize(image, dim)
    resizename = path + '/thumbnails/thumb_' + imagename
    cv2.imwrite(resizename, resize)
    return resizename


#------------------------------------------------
# Format links
#------------------------------------------------
def format_link_md(completefilename):
    return "![screenshot](" + completefilename + ")"

def format_link_zim(completefilename):
    return "{{file:///" + completefilename.replace('\\', '/') + "?width=600}}"

def format_link_org(completefilename, resizename):
    return "[[file:" + resizename + "]]\n" + '@@html:<a href="' + completefilename +'"></a>@@'

def get_month():
    return str(datetime.today().month).zfill(2)

#------------------------------------------------
# Format links
#------------------------------------------------
if __name__ == "__main__":
    folder = input ("== Screen capture Rafale ==\nProvide a folder [current month]: ")
    if folder == "":
        folder = get_month()
    targetdir = os.path.join(TARGET, folder)
    if not os.path.isdir(targetdir):
        os.makedirs(targetdir)
    image = ""
    shotnumber = 0
    devicenumber = 1
    outputformat = FORMAT_ORG
    q = input("Device? [1] ")
    if q == "2":
        devicenumber = 2
    meeting_name = input("Meeting name [meeting]:")
    if meeting_name == "":
        meeting_name = "meeting"
    form = input("Format (zim, md, org)? [org] ")
    if form == "zim":
        outputformat = FORMAT_ZIM
    elif form == "md":
        outputformat = FORMAT_MD
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
        newfilename = datetime.now().strftime("%Y%m%d_%H%M%S_%f") + '_' + meeting_name + ".png"

        # Strange behavior on Windows: backslash is introduced
        # completefilename = os.path.join(targetdir, newfilename)

        completefilename = targetdir + '/' + newfilename 
        os.rename(os.path.join(os.getcwd(),image), completefilename)
        print("Generated file: " + completefilename)
        if outputformat == FORMAT_MD:
            temp = format_link_md(completefilename)
            all_links.append(temp)
            pyperclip.copy(temp)
            print("Filename copied to clipboard (md format)")
        elif outputformat == FORMAT_ORG:
            # The treatment is slightly different because it must appear in emacs
            # as a thumbnail
            resizename = resize_image(targetdir, newfilename)
            # temp = format_link_org(completefilename)
            #temp = format_link_org(resizename)
            temp = format_link_org(completefilename, resizename)
            all_links.append(temp + "\n")
            pyperclip.copy(temp)
            print("Filename copied to clipboard (org format)")
        else:
            temp = format_link_zim(completefilename)
            all_links.append(temp)
            pyperclip.copy(temp)
            print("Filename copied to clipboard (zim format)")
        
    
