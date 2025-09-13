########################################################
# Tools for the Finance data processing
# O. Rey - September 2024
########################################################
import csv, time, os.path
from datetime import datetime

#---------------- In order to use in other files
#
#import sys
#sys.path.append('.')
#from tools import
# Timer, countLinesInCSVFile, interrupt, myprint, ensureFile, generateName, myexit
#

#============================================ generateName
def myexit(msg):
    myprint(msg)
    myprint("Exiting")
    exit()


#============================================ generateName
def generateName(name):
    return datetime.now().strftime('%Y%m%d_%H%M%S-%f') + name


#============================================ ensureFile
def ensureFile(input, verbose = False):
    if not os.path.isfile(input):
        if verbose: print("File '" + input + "' not found. Exiting...")
        return False
    return True

#============================================ ensureFile
def ensureFolder(input, verbose = False):
    if not os.path.isdir(input):
        if verbose: print("Folder '" + temp + "' not found. Exiting...")
        return False
    return True

#============================================ myprint
LOG = "run.log"
FIRST = True
def myprint(str):
    '''
    print to console and into a log file
    '''
    global FIRST
    if FIRST:
        with open(LOG, "w",encoding='utf-8') as logfile:
            logfile.write(str + '\n')
        FIRST = False
    else:
        with open(LOG, "a",encoding='utf-8') as logfile:
            logfile.write(str + '\n')
    print(str)
        

#============================================ interrupt
def interrupt(obj=None):
    '''
    Manual breakpoint
    '''
    if obj != None:
        print(obj)
    resp = input("Continue? ")
    if resp.upper() in ["n", "no", "N","NO"]:
        print("Goodbye!")
        exit(0)


#=========================================== count lines in csv file
def countLinesInCSVFile(file):
    newreader = csv.reader(open(file, "r", encoding='utf-8', errors='ignore'))
    nblines = 0
    for i, row in enumerate(newreader):
        nblines += 1
    return nblines

        
#============================================ Timer
class Timer():
    def __init__(self):
        self.start = time.time()
    def stop(self):
        self.stop = time.time()
        print("\nTreatment duration: "
              + str((round(self.stop-self.start))//60)
              + " minutes and "
              + str((round(self.stop-self.start))%60)
              + " seconds\n")
        

