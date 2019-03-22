#!/bin/python3
import os, markdown, codecs

if __name__ ==  "__main__":
    ifile = input("Name of the file to convert (without md extension): ")
    
    input_file = codecs.open(ifile + ".md", mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)
    output_file = codecs.open(ifile + ".html",
                              "w",
                              encoding="utf-8",
                              errors="xmlcharrefreplace")
    output_file.write(html)
    print("File generated")


    
