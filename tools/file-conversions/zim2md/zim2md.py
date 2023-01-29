#!/bin/python3

import sys, os, codecs, glob

from pathlib import Path

# MYPATH = "C:/Users/a876246/Documents/oreyboulot-Airbus/Airbus Helicopters/__minutes/"
MYPATH = "C:/ProgramData/orey/Temp/"

#--- key:org, value:md
#--- Start of line
RULE_HEAD = {"= ": "# ",
             "== ": "## ",
             "=== ": "### ",
             "==== ": "#### ",
             "===== ": "##### ",
             "-":"*",
             "  -":"  *",
             "    -":"    *"}

#--- Underline, bold, italics
#--- symetrical rules
#--- key:org, value:md
RULE_LINE = {"__":"_",
             "/":"_"}

#--- unsymetrical rule
RULE_LINK = {"[[|]]":"[Lien](|)"}


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


def convert(sourcefile, targetfile):
    """ Convert """
    input = codecs.open(sourcefile, mode="r", encoding="utf-8", errors='ignore')
    output = codecs.open(targetfile, mode="w", encoding="utf-8")
    content = input.readlines()
    for line in content:
        output.write(convert_line(line))
    input.close()
    output.close()



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
    print(convert_line("du texte avec un lien fichier file:../toto/titi.txt "))
    print(convert_line("du texte avec un lien fichier file:../toto/titi.txt"))
    


def ask_for_input_dir(rootdir, msg):
    dirname = input(msg)
    fulldirname = os.path.join(rootdir, dirname)
    while True:
        if os.path.isdir(fulldirname):
            return fulldirname
        else:
            print(fulldirname + " is not a valid directory. Try again...")

            
def ask_for_input_file(rootdir, msg):
    while True:
        filename = input(msg)
        fullfilename = os.path.join(rootdir, filename)
        if os.path.isfile(fullfilename):
            return filename, fullfilename
        else:
            print(filename + " is not a valid file. Try again...")

            
def ask_for_output_dir(rootdir, msg):
    dirname = input(msg)
    fulldirname = os.path.join(rootdir, dirname)
    if os.path.exists(fulldirname) and os.path.isdir(fulldirname):
        return fulldirname
    else:
        os.makedirs(fulldirname)
        return fulldirname

    
def change_extension(filename, old_ext, new_ext):
    if filename.split('.')[-1] != old_ext:
        print("Not an " + old_ext + " file. Exiting...")
        sys.exit(1)
    return filename.split('.')[-2] + '.' + new_ext
    

if __name__ ==  "__main__":
    print("=== zim2md converter")
    print("=== Configured path: " + MYPATH)
    fulldirname = ask_for_input_dir(MYPATH,
                                    "=== Provide a relative folder [folder/subfolder/.../subfolder]: ")
    targetdir = ask_for_output_dir(MYPATH,
                                   "=== Provide a relative output dir: ")
    convertall = input("=== Convert all files in folder? [n/y] ")
    if not convertall == "y":
        filename, fullfilename = ask_for_input_file(fulldirname,
                                                    "=== Provide the filename to convert: ")
        newfilename = change_extension(filename, "txt", "md")
        targetfile = os.path.join(targetdir, newfilename)
        convert(fullfilename, targetfile)
    else:
        flist = glob.glob(fulldirname + "/*.org")
        for f in flist:
            newfilename = os.path.join(targetdir, change_extension(os.path.split(f)[1], "txt", "md"))
            convert(f, newfilename)
            print(f + " file converted")
            

