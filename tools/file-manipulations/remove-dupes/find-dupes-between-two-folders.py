###########################################################
# Dedupe 2 folders
# rey.olivier@gmail.com
# August 15 2024
###########################################################
import os, sys, shutil, getopt, hashlib
from time import time
from datetime import datetime

# Global constants
GARBAGE = '/tmp/'
TIMESTAMP = 'filesync_' + datetime.now().strftime('%Y%m%d_%H%M%S-%f')

# Works with interrupt
DEBUG = True


#============================================ interrupt
def interrupt(text=""):
    '''
    Manual breakpoint
    '''
    if DEBUG == True:
        if text != "":
            print(text)
        resp = input("Continue? ")
        if resp.upper() in ["N","NO"]:
            print("Goodbye!")
            exit(0)


#============================================ sha256sum
def sha256sum(completefilename):
    '''
    Unique footprint of the file
    '''
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(completefilename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()


#============================================ ensure folder
def ensure_folder(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)

        
#============================================ garbage
def garbage(filename):
    # Garbaging file is just moving it for safety
    garb = os.path.join(GARBAGE, TIMESTAMP)
    if not os.path.isdir(garb):
        os.mkdir(garb)
        print("Garbage folder " + garb + " created")
    timestamp = str(time()).split('.')[0] + str(time()).split('.')[1]
    #get just filename
    fil = filename.split('/')[-1]
    try:
        shutil.move(filename, os.path.join(garb, timestamp + '-' + fil))
    except Exception as err:
        print(err)

        
#============================================ analyze source
def analyze_reference(path):
    '''
    Creates a dict with {sha : fullpath/filename.ext}
    '''
    dict = {}
    count = 0
    for root, dirs, files in os.walk(path):
        if DEBUG:
            print(dirs)
        for thefile in files: 
            count +=1
            # calculating the value
            completefilename = os.path.join(root,thefile)
            hash = str(sha256sum(completefilename))
            dict[hash]=completefilename
            #interrupt(dict)
            sys.stdout.write(str(count) + '|')
            sys.stdout.flush()
    print("\n--- " + str(count) + " files found in " + path)
    return dict


#============================================ analyze source
def analyze_temp(path, dict, analyzemode):
    '''
    Creates a dict with {sha : fullpath/filename.ext}
    '''
    count = 0
    for root, dirs, files in os.walk(path):
        if DEBUG:
            print(dirs)
        for thefile in files: 
            count +=1
            # calculating the value
            completefilename = os.path.join(root,thefile)
            hash = str(sha256sum(completefilename))
            sys.stdout.write(str(count) + '|')
            sys.stdout.flush()
            if hash in dict:
                print("\nDuplicate: " + completefilename + " === " + dict[hash])
                if not analyzemode:
                    garbage(completefilename)
                    print("In garbage: " + completefilename)
    print("\n--- " + str(count) + " files compared from " + path)
    return count


#============================================ usage
def usage():
    print("Analyze 2 folders to find the duplicates")
    print("Usage: \n $ filesync -r [REFERENCE_FOLDER] -t [TEMP_FOLDER] (-a) (-h)")
    print("-REFERENCE_FOLDER and TEMP_FOLDER are mandatory parameters")
    print("-'-a' is just doing an analysis of the deltas")
    print("-'-h' is for help")
    sys.exit(0)    

    
#============================================ analyze target
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "r:t:g:adh",
                                   ["ref=", "temp=", "garbage=", "analyze", "debug", "help"])
    except getopt.GetoptError:
        usage()
    if len(opts) == 0:
        usage()
    analyzemode = False
    garbage = ""
    reference = ""
    temp = ""
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        if o in ("-d", "--debug"):
            print("Debug mode activated")
            global DEBUG
            DEBUG = True
        if o in ("-a", "--analyze"):
            analyzemode = True
        if o in ("-g", "--garbage"):
            if not os.path.isdir(a):
                print("Garbage folder '" + a + "' does not exist. Maybe there is a typo in the name. Exiting.")
                sys.exit()
            global GARBAGE
            GARBAGE = a
        if o in ("-r", "--ref"):
            if not os.path.isdir(a):
                print("Reference folder '" + a + "' does not exist. Maybe there is a typo in the name. Exiting.")
                sys.exit()
            reference = a
        if o in ("-t", "--temp"):
            if not os.path.isdir(a):
                print("Temp folder '" + a + "' does not exist. Maybe there is a typo in the name. Exiting.")
                sys.exit()
            temp = a   
    #local = "/home/olivier/JDR-RPG/JDR/Ambre/"
    #remote = "/run/user/1000/gvfs/ftp:host=ls-wxl271.local/array1/DisqueBuffaloRaid1/JDR-RPG/JDR/Ambre/"
    dict = analyze_reference(reference)
    #print(dict)
    analyze_temp(temp, dict, analyzemode)
    
    
if __name__ == "__main__":
    main()
        
        
        

