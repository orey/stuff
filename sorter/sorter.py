#---------------------------------
#-- Sorter python script
#-- Copyleft Olivier Rey 2018
#-- This utility sorts files and creates a timeline tree
#-- It is working per type
#---------------------------------

import hashlib
import sys

from os import listdir
from os.path import isfile, join


FOLDER = '/home/olivier/.aMule/Incoming/'
EXT = '.pdf'

DICT = {}

def getFilesInFolder(mypath):
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]


def getHash(myfile):
    hasher = hashlib.md5()
    with open(myfile, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def main():
    files = getFilesInFolder(FOLDER)
    print("== Folder: " + FOLDER)
    print("== " + str(len(files)) + " files found")
    dupes = 0
    keys = 0
    for f in files:
        completename = FOLDER + f
        h = getHash(completename)
        keys +=1
        sys.stdout.write(str(keys) + "|")
        sys.stdout.flush()
        try:
            temp = DICT[h]
            print('\n== Found duplicate of ' + "'" + completename + "'")
            print("== '" + temp + "'")
            dupes += 1
        except KeyError:
            DICT[h] = completename
    print("\n== Generated " + str(len(DICT)) + " MD5 keys")

if __name__ == "__main__":
    main()






