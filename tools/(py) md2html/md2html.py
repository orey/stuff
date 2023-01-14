#!/bin/python3
import os, markdown, codecs

MYPATH = "C:/Users/Toto/path/to/minutes/"
MINUTES = "minutes.md"

if __name__ ==  "__main__":
    fulldirname = None
    while True:
        folder = input("Name of the folder: ")
        fulldirname = os.path.join(MYPATH, folder)
        if not os.path.isdir(fulldirname):
            print('"' + fulldirname + '" is not a folder.')
        else:
            break
    fullfilename = os.path.join(fulldirname, MINUTES)
    input_file = codecs.open(fullfilename, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)
    output_file = codecs.open(os.path.join(fulldirname, "minutes.html"),
                              "w",
                              encoding="utf-8",
                              errors="xmlcharrefreplace")
    output_file.write(html)
    print("File generated")

