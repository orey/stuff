#!/bin/python3
import sys, os
import networkx as nx


def usage():
    print("Usage:")
    print("> python gml2txt.py [filename.gml]")

if __name__ ==  "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    inputfile = sys.argv[1]
    print(inputfile)
    targetfile = inputfile.replace('.gml', '') + ".txt"
    g = nx.read_gml(inputfile)
    print(g)
    l = len(g)
    print(l)
    with open(targetfile, 'w') as f:
        for i in range(0,l):
            print(g.node[i])
            f.write(g.node[i]['label'])
        f.close()
    print("File generated")

