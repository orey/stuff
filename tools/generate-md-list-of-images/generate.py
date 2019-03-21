import os, sys
from os import listdir
from os.path import isfile, join

print('== Generates a md file that points to all images ==')

mypath = os.getcwd()

relativedir = mypath.split('\\')[-1]
fname = relativedir.replace(" ","") + ".md"

print("File name: " + fname)

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

count = 0
with open(fname, 'w') as fil:
    fil.write("# " + relativedir + "\n\n")
    for f in onlyfiles:
        if f.endswith('.PNG') or f.endswith('.png'):
            count += 1
            fil.write("![Image" + str(count) + "](" + f + ")\n\n")
            print(f)
fil.close()

