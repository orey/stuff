#!/bin/python3

#import sys, os, markdown, codecs

import sys

from pathlib import Path

MYPATH = "C:/Users/a876246/Documents/oreyboulot-Airbus/Airbus Helicopters/__minutes/"

RULE_HEAD = {"* ": "# ", "** ": "## ", "*** ": "### ", "**** ": "#### ", "***** ": "##### ", "-":"*", "  -":"  *", "    -":"    *"}

#--- Underline, bold, italics, link
RULE_LINE = {"_|_":"|", "*|*":"**|**", "/|/":"_|_", "[[|]]":"!(|)"}


def convert_line(str):
    newstr = ""
    cursor = 0
    for key in RULE_HEAD:
        if str.startswith(key):
            newstr = RULE_HEAD[key]
            cursor = len(newstr)
    tempstr = str[cursor:]
    for key in RULE_LINE:
        rule = key.split("|")
        if tempstr.startswith(rule[0]) and tempstr[len(begin)]!=" ":
            #search for the end
    return newstr

def convert_text()



def convert(f):
    """ Convert """
    print(f.name)
    print(convert_line("** Test et olé"))

    
if __name__ ==  "__main__":
    folder = None
    consopath = ""
    myfile = None
    if len(sys.argv) != 0:
        print("=== Debug mode")
        myfile = Path(MYPATH + "org/2020/202001.org")
        if myfile.is_file():
            convert(myfile)
            sys.exit(0)
        else:
            print("error")
            sys.exit(1)
    print("=== org2md converter")
    print("=== Configured path: " + MYPATH)
    while True:
        consopath = MYPATH + input("=== Provide a relative folder [folder/subfolder/.../subfolder]: ")
        folder = Path(consopath)
        if folder.is_dir():
            break;
        else:
            print(consopath + ": Not a valid directory")
    while True:
        temp = consopath + "/" + input("=== Provide the filename to convert: ")
        myfile = Path(temp)
        if myfile.is_file():
            break;
        else:
            print(temp + ": Not a valid file")
    convert(myfile)
    


            
    print("Success: " + consopath + " is a folder")
    print("Success: " + myfile.name + " is a file")
    
