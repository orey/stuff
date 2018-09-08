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
import PIL.Image
import PIL.ExifTags

from datetime import datetime
from os import listdir
from os.path import isfile, join
from shutil import copyfile


FOLDER = '/home/olivier/.aMule/Incoming/'
EXT = '.jpg'
MINSIZE = 5000
MAXSIZE = 15000000

DATETAG1 = 'DateTimeOriginal'
DATETAG2 = 'DateTimeDigitized'

DATETIME1 = 'created'
DATETIME2 = 'lastmodif'

VERBOSE = True

DUP = 'duplicates'
SORTED = 'sorted'
ROOT = '/home/olivier/Temp'


def copyFile(src, key, dest):
    if not os.path.isfile(src):
        print("== Error: " + src + " is not a valid file") 
        return False
    if not os.path.isdir(dest):
        print("== Error: " + dest + " is not a valid folder")
    filename = os.path.basename(src)
    l = len(filename)
    temp = key + '_' + filename[:l-4] + EXT
    if os.path.isfile(temp):
        print("== Error: file " + temp + " already exists. Skipping...")
        return False
    tfn = join(dest, temp)
    copyfile(src, tfn)
    return True

def analyzePhoto(photo):
    d = getExif(photo)
    if not d == None:
        a =  d[DATETAG1]
        b =  d[DATETAG2]
        if VERBOSE:
            print(a)
            print(b)
        if a > b:
            return createName(b)
        else:
            return createName(a)
    d = getFileDate(photo)
    a = d[DATETIME1]
    b = d[DATETIME2]
    if VERBOSE:
        print(a)
        print(b)
    if a > b:
        return createName(b)
    else:
        return createName(a)
        


def testCopyFile():
    p = '/home/olivier/photo.jpg'
    key = analyzePhoto(p)
    r = copyFile(p, key, '/home/olivier/Temp')
    if r:
        print("OK")
    else:
        print("NOT OK")

    
def createFolder(mypath):
    if not os.path.isdir(mypath):
        os.makedirs(mypath)


def createRoot(mypath):
    myroot = join(mypath, SORTED + "_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
    createFolder(myroot)
    sorted = join(myroot, SORTED)
    createFolder(sorted)
    dup = join(myroot, DUP)
    createFolder(dup)
    return sorted, dup
    
def testCreateRoot():
    createRoot(ROOT)



def createName(dtime):
    return dtime.strftime("%Y%m%d_%H%M%S_%f")

def getExif(photo):
    """
    Extract photo datetime metadata or None
    """
    f = PIL.Image.open(photo)
    if f._getexif() == None:
        return None
    datetags = [DATETAG1,DATETAG2]
    exif = {}
    for k, v in f._getexif().items():
        a = PIL.ExifTags.TAGS[k]
        #print(a)
        for tag in datetags:
            if a == tag:
                exif[tag] = v
    return exif
    
def testGetExif():
    file1 = '/home/olivier/photo.jpg'
    file2 = '/home/olivier/photo2.jpg'
    d = getExif(file1)
    print(d)
    e = getExif(file2)
    print(e)
    a = getFileDate(file1)
    print(a)
    print(getFileDate(file2))
    print("Name of the file would be : " + createName(a['lastmodif']))
          
    

def getFileDate(file):
    return { DATETIME1 : datetime.fromtimestamp(os.path.getctime(file)), \
             DATETIME2 : datetime.fromtimestamp(os.path.getmtime(file)) }
    

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
    if (not completename.endswith(EXT)) and (not completename.endswith(EXT.upper())) :
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
    """
    Generate hash for several algorithms
    """
    hasher = None
    if algo == 1:
        hasher = hashlib.sha1()
    else:
        hasher = hashlib.md5()
    with open(myfile, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()



def createDict(dict, folder, algo=0):
    """
    Creates a dict with a hash and the file in order to spot the duplicate files
    even if they don't have the same names
    """
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
            print('\n== Found duplicate of ' + "'" + completename + "'")
            print("== '" + temp + "'")
            dupes += 1
            # Create folder for dup
            
        except KeyError:
            dict[h] = completename
    if len(folders) == 0 or folders == None:
        return dict
    for d in folders:
        createDict(dict, d, algo)
    return dict

def compareHash():
    global VERBOSE
    VERBOSE = False
    start1 = time.time()
    dict1 = {}
    createDict(dict1, '/home/olivier/.aMule/Incoming')
    end1 = time.time()

    start2 = time.time()
    dict2 = {}
    createDict(dict2, '/home/olivier/.aMule/Incoming', 1)
    end2 = time.time()

    print("\n== Generated " + str(len(dict1)) + " MD5 keys")
    print("== Execution time with md5: " + str(end1 - start1))
    print("\n== Generated " + str(len(dict2)) + " SHA1 keys")
    print("== Execution time with sha1: " + str(end2 - start2))
    

def testSorted():
    dict = {}
    createDict(dict, '/home/olivier/MEGA/Images-photos', 1)
    
    
if __name__ == "__main__":
    #main()
    #testGetFilesInFolder()
    #compareHash()
    #testGetExif()
    #testCreateRoot()
    testSorted()
    testCopyFile()






