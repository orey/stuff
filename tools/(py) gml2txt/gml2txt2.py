#!/bin/python3
import sys, os

def usage():
    print("Usage:")
    print("> python gml2txt2.py [filename.gml]")

if __name__ ==  "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    inputfile = sys.argv[1]
    print(inputfile)
    targetfile = inputfile.replace('.gml', '') + ".txt"
    with open(inputfile, 'r') as inp:
        content = inp.readlines()
        with open(targetfile, 'w') as f:
            for line in content:
                if line.lstrip().startswith('label'):
                    line2 = line.replace('label', '').lstrip().replace('"','').rstrip()
                    print(line2)
                    f.write(line2 + '\n')
            f.close()
        inp.close()
    print("File generated")

