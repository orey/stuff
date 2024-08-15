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
def analyze_temp(path, dict):
    '''
    Analyze the files 
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






#============================================ usage
def usage():
    print("Analyze 2 folders to find the duplicates")
    print("Usage: \n $ filesync -s [SOURCE_FOLDER] -t [TARGET_FOLDER] (-a) (-h)")
    print("-SOURCE_FOLDER and TARGET_FOLDER are mandatory parameters")
    print("-'-a' is just doing an analysis of the deltas")
    print("-'-h' is for help")
    sys.exit(0)    

    
#============================================ analyze target
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:t:g:adh",
                                   ["source=", "target=", "garbage=", "analyze", "debug", "help"])
    except getopt.GetoptError:
        usage()
    if len(opts) == 0:
        usage()
    analyzemode = False
    garbage = ""
    source = ""
    target = ""
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
        if o in ("-s", "--source"):
            if not os.path.isdir(a):
                print("Source folder '" + a + "' does not exist. Maybe there is a typo in the name. Exiting.")
                sys.exit()
            source = a
        if o in ("-t", "--target"):
            if not os.path.isdir(a):
                print("Target folder '" + a + "' does not exist. Maybe there is a typo in the name. Exiting.")
                sys.exit()
            target = a   
    #local = "/home/olivier/JDR-RPG/JDR/Ambre/"
    #remote = "/run/user/1000/gvfs/ftp:host=ls-wxl271.local/array1/DisqueBuffaloRaid1/JDR-RPG/JDR/Ambre/"
    dict = analyze_reference(source)
    print(dict)
    #analyze_target(target, dict, analyzemode)

    
if __name__ == "__main__":
    main()
        
        
        

