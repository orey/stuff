#!/bin/python3
import sys
from xml.dom import minidom

def usage():
    print("Usage:")
    print("> python graphml-label-extractor.py [filename.graphml]")
    print("Generates a [filename.txt] with all labels")

if __name__ ==  "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    inputfile = sys.argv[1]
    targetfile = inputfile.replace('.graphml', '') + ".txt"

    xmldoc = minidom.parse(inputfile)
    itemlist = xmldoc.getElementsByTagName('y:NodeLabel')
    print("Number of node labels found:" + str(len(itemlist)))
    with open(targetfile, 'w') as f:
        for elem in itemlist:
            try:
                print(elem.firstChild.nodeValue)
                f.write(elem.firstChild.nodeValue + '\n')
            except:
                pass
        f.close()
    print("File generated")

