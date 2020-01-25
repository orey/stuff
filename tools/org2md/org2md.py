#!/bin/python3

#import sys, os, markdown, codecs

import sys, codecs

from pathlib import Path

MYPATH = "C:/Users/a876246/Documents/oreyboulot-Airbus/Airbus Helicopters/__minutes/"

#--- key:org, value:md
#--- Start of line
RULE_HEAD = {"* ": "# ",
             "** ": "## ",
             "*** ": "### ",
             "**** ": "#### ",
             "***** ": "##### ",
             "-":"*",
             "  -":"  *",
             "    -":"    *"}

#--- Underline, bold, italics
#--- symetrical rules
#--- key:org, value:md
RULE_LINE = {"_":"",
             "*":"**",
             "/":"_"}

#--- unsymetrical rule
RULE_LINK = {"[[|]]":"!(|)",
             "file:| ":"(|)"}


def convert_line(stri):
    newstr = ""
    cursor = 0
    for key in RULE_HEAD:
        if stri.startswith(key):
            newstr = stri.replace(key, RULE_HEAD[key])
            return newstr
    newstr = stri
    for key in RULE_LINE:
        le = len(key)
        inds = newstr.find(key)
        inde = newstr.find(key, inds+le)
        if inds != -1 \
           and inde !=-1 \
           and newstr[inds+le] != " " \
           and newstr[inde-le] != " " \
           and (inds == 0 or newstr[inds-1] == " ") \
           and (inde == len(newstr)-1 or newstr[inde+le]==" "):
            rep = RULE_LINE[key]
            newstr = newstr.replace(key, rep, 2)
    for key in RULE_LINK:
        bkey = key.split("|")[0]
        leb = len(bkey)
        ekey = key.split("|")[1]
        lee = len(ekey)
        inds = newstr.find(bkey)
        inde = newstr.find(ekey, inds+1)
        if inds != -1 and inde !=-1 \
           and newstr[inds+leb] != " " \
           and newstr[inde-1] != " " \
           and (inds == 0 or newstr[inds-1] == " ") \
           and (inde == len(newstr)-lee or newstr[inde+lee]==" "):
            newstr = newstr.replace(bkey, RULE_LINK[key].split("|")[0])
            newstr = newstr.replace(ekey, RULE_LINK[key].split("|")[1])
    return newstr


def convert(f):
    """ Convert """
    print(f.name)
    test()
    with f.open(encoding="utf-8") as ff:
        content = ff.readlines()
        for line in content:
            print(convert_line(line))
            

    
def test():
    print(convert_line("** Titre2"))
    print(convert_line("* Titre 1"))
    print(convert_line("*** Titre 3 et oula"))
    print(convert_line("**** Titre 4Test et olé"))
    print(convert_line("***** Titre 5"))
    print(convert_line("*C'est en bold*"))
    print(convert_line("* C'est pas du bold c'est un titre*"))
    print(convert_line(" * C'est pas du bold 1*"))
    print(convert_line(" *C'est pas du bold 2 *"))
    print(convert_line("Du *bold avec du texte* dans un autre texte"))
    print(convert_line("Blah blah _underligned here_"))
    print(convert_line("Blah blah _underligned here_    ggsgsg"))
    print(convert_line("[[/un/lien/vers/le/paradis.png]]"))
    print(convert_line("[[ /un/lien/vers/le/paradis.png]]"))
    print(convert_line("[[/un/lien/vers/le/paradis.png ]]"))
    print(convert_line("du texte [[/un/lien/vers/le/paradis.png]] encore du texte"))
    print(convert_line("du texte avec un lien fichier

    
    

    
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
    
