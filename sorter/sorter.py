#---------------------------------
#-- Sorter python script
#-- Copyleft Olivier Rey 2018
#-- This utility sorts files and creates a timeline tree
#-- It is working per type
#---------------------------------

import hashlib
import sys
import time
import os

from os import listdir
from os.path import isfile, join


FOLDER = '/home/olivier/.aMule/Incoming/'
EXT = '.pdf'
MINSIZE = 5000
MAXSIZE = 15000000

VERBOSE = True


def convertBytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def fileOK(completename):
    """
    Filters the files not to generate hash for too small or too big
    files or for files with the wrong extension
    """
    if not completename.endswith(EXT):
        return False
    fsize = os.stat(completename).st_size
    if fsize > MAXSIZE:
        if VERBOSE: print("== File: " + completename + " too big (" + \
                         convertBytes(fsize) + "). Excluding.")
        return False
    elif fsize < MINSIZE:
        if VERBOSE: print("== File: " + completename + " too small (" + \
                         convertBytes(fsize) + "). Excluding.")
        return False
    else:
        return True


def getFilesInFolder(mypath):
    """
    Returns two lists, the list of files and the list of subfolders
    All is managed with complete names
    The list of files is filtered
    """
    glob = listdir(mypath)
    files = []
    folders = []
    for f in glob:
        completef = join(mypath,f)
        if isfile(completef):
            if fileOK(completef):
                files.append(completef)
        else:
            folders.append(completef)
    return files, folders


def testGetFilesInFolder():
    files, folders = getFilesInFolder('/home/olivier/.aMule/Incoming')
    print("== Files:")
    print(files)
    print("== Folders:")
    print(folders)

def getHash(myfile, algo=0):
    hasher = None
    if algo == 1:
        hasher = hashlib.sha1()
    else:
        hasher = hashlib.md5()
    with open(myfile, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()


def createDict(folder, algo=0):
    """
    Creates a dict with a hash and the file in order to spot the duplicate files
    even if they don't have the same names
    """
    dict = {}
    files, folders = getFilesInFolder(folder)
    if VERBOSE:
        print("== Folder: " + folder)
        print("== " + str(len(files)) + " files found with matching filter")
    dupes = 0
    keys = 0
    for completename in files:
        h = getHash(completename, algo)
        keys +=1
        sys.stdout.write(str(keys) + "|")
        sys.stdout.flush()
        try:
            temp = dict[h]
            if VERBOSE:
                print('\n== Found duplicate of ' + "'" + completename + "'")
                print("== '" + temp + "'")
            dupes += 1
        except KeyError:
            dict[h] = completename
    return dict

def compareHash():
    start1 = time.time()
    dict1 = createDict('/home/olivier/.aMule/Incoming')
    end1 = time.time()

    start2 = time.time()
    dict2 = createDict('/home/olivier/.aMule/Incoming', 1)
    end2 = time.time()

    print("\n== Generated " + str(len(dict1)) + " MD5 keys")
    print("== Execution time with md5: " + str(end1 - start1))
    print("\n== Generated " + str(len(dict2)) + " SHA1 keys")
    print("== Execution time with sha1: " + str(end2 - start2))
    

    
if __name__ == "__main__":
    #main()
    #testGetFilesInFolder()
    compareHash()






