import hashlib
import sys
import time
import os
import getopt

from os import listdir
from os.path import isfile, isdir, join

REL_SOURCE = ''


# --------------------------------------------
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


# --------------------------------------------
def getFilesInFolder(mypath):
    """
    Returns two lists, the list of files and the list of subfolders
    All is managed with complete names
    """
    try:
        glob = listdir(mypath)
        files = []
        folders = []
        for f in glob:
            completef = join(mypath,f)
            if isfile(completef):
                files.append(completef)
            else:
                folders.append(completef)
        return files, folders
    except Exception:
        print("== Problem with folder: " + mypath)
        return None, None


# --------------------------------------------
def createDict(dict, folder, algo=0, verbose=False):
    """
    Creates a dict with a hash and the file in order to spot the duplicate files
    even if they don't have the same names
    Warning: This function is recursive.
    """
    files, folders = getFilesInFolder(folder)
    if verbose:
        print("\n== Folder: " + folder)
    if files != None:
        keys = 0
        for completename in files:
            h = getHash(completename, algo)
            keys +=1
            sys.stdout.write(str(keys) + "|")
            sys.stdout.flush()
            dict[h] = completename
    if folders != None:
        for d in folders:
            createDict(dict, d, algo, verbose)
    return dict



# --------------------------------------------
def usage():
    '''
    Usage function
    '''
    print('Usage:')
    print('> python -i C:/source_folder -o C:/target_folder')
    print('Other options:')
    print('"-v" verbose mode')
    print('"-h" usage')


# --------------------------------------------
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:hvt",
                                   ["inputdir=", \
                                   "outputdir=","help", \
                                   "verbose", "test"])
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)
    # init option keys
    inputdir = ""
    outputdir = ""
    verbose = False
    test    = False
    # parsing options
    for k, v in opts:
        if k in ("-h", "--help"):
            usage()
            sys.exit(0)
        if k in ("-i", "--inputdir"):
            inputdir = v
        if k in ("-o", "--outputdir"):
            outputdir = v
        if k in ("-v", "--verbose"):
            verbose = True
        if k in ('-t', '--test'):
            test = True
    # Do stuff
    if test == False:
        print("Not implemented")
        sys.exit(0)
    if not isdir(inputdir):
        print(inputdir + " not a directory. Exiting...")
        sys.exit(0)
    mydict = {}
    LENGTH_SOURCE = len(inputdir)
    if inputdir[-1] == '/' or inputdir[-1] == '\\':
        inputdir = inputdir[0,LENGTH_SOURCE-1]
    createDict(mydict, inputdir, 0, True)
    print(mydict)





if __name__ == "__main__":
    main()

