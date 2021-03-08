#!/bin/python3
import sys, os
import sqlite3
import pathlib

DBNAME = "allfiles.db"
OUTPUT = "output.txt"
COUNT = 0
ROOT_ONE = ""

def getListOfFiles(dirName, f, conn):
    global COUNT, ROOT_ONE
    c = conn.cursor()
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    #allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            getListOfFiles(fullPath, f, conn)
        else:
            f.write(fullPath + '\n')
            # storing root and relative folder
            c.execute("INSERT INTO files VALUES (?, ?, ?, ?, ?)", \
                      (ROOT_ONE, \
                       dirName.split(ROOT_ONE + '\\')[1], \
                       entry, \
                       os.path.getmtime(fullPath), \
                       os.path.getsize(fullPath)))
            COUNT = COUNT + 1
            sys.stdout.write(str(COUNT) + '|')
            sys.stdout.flush()
    conn.commit()
    sys.stdout.write('commit|')
    sys.stdout.flush()
    


def master(dirName):
    global COUNT, ROOT_ONE
    ROOT_ONE = dirName[0:len(dirName)-1] if dirName[-1] == '\\' else dirName
    # Create DB
    conn = sqlite3.connect(DBNAME)
    c = conn.cursor()
    # Create table
    try:
        c.execute("DROP TABLE files")
        print("Old table dropped")
    except:
        print("Starting fresh")
    
    c.execute('''CREATE TABLE files (root TEXT, folder TEXT, file TEXT, time REAL, size INT)''')
    # Create file
    with open(OUTPUT, 'w') as f:
        getListOfFiles(dirName, f, conn)
    # Close file
    f.close()
    # Close DB
    conn.close()
    print("\n=> " + str(COUNT) + " files examined")

    
    
def usage():
    print("Usage:")
    print("> python synchro.py [folder]")


if __name__ ==  "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    # get list of files from the console
    inputdir = sys.argv[1]
    # Get the list of all files in directory tree at given path
    master(inputdir)
    print("Done")

