###########################################################
# Synchronize folders and thier content
# rey.olivier@gmail.com
# August 11 2024
###########################################################
import os, sys, shutil, getopt
import hashlib
from time import time
from datetime import datetime

# Global constants
GARBAGE = '/tmp/'
TIMESTAMP = 'filesync_' + datetime.now().strftime('%Y%m%d_%H%M%S-%f')

# Works with interrupt
DEBUG = False


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
def analyze_source(path):
    '''
    Creates a dict with {relativepath/filename.ext : fullpath/filename.ext}
    '''
    dict = {}
    count = 0
    for root, dirs, files in os.walk(path):
        if DEBUG: print(dirs)
        for thefile in files: 
            count +=1
            # calculating the value
            completefilename = os.path.join(root,thefile)
            relativefilename = completefilename.split(path)[1]
            dict[relativefilename]=completefilename
            #interrupt(dict)
            sys.stdout.write(str(count) + '|')
            sys.stdout.flush()
    print("\n--- " + str(count) + " files found in " + path)
    return dict


#============================================ analyze target
def analyze_target(path, sourcedict, analyze=False):
    '''
    We are treating the target while analyzing it
    '''
    count = 0
    for root, dirs, files in os.walk(path):
        if DEBUG: print(dirs)
        for thefile in files: 
            count +=1
            completefilename = os.path.join(root,thefile)
            relativefilename = completefilename.split(path)[1]
            try:
                # 1. Skip the identical files located at the same place
                completesourcefilename = sourcedict[relativefilename]
                print("Same file at the same place: " + relativefilename)
                interrupt()
                # Remove from sourcedict
                del sourcedict[relativefilename]
            except KeyError:
                # 2. Remove target files that are not in the source
                #print(sys.exception())
                if analyze:
                    print("To remove from target: " + relativefilename)
                else:
                    print("File existing in target but not in source. Garbaging: " + completefilename + " ... ",end="", flush=True)
                    interrupt()
                    garbage(completefilename)
                    print("Done.")
    # 3. Create target files (and folders) based on existing source files that are not in target
    for key,value in sourcedict.items():
        filetocreate = os.path.join(path,key)
        # check if folders exist
        lis = key.replace(key.split('/')[-1], "").split('/')
        if len(lis) > 1 and not analyze:
            cumul = path
            for i in range(0, len(lis)-1):
                ensure_folder(os.path.join(cumul,lis[i]))
                cumul = os.path.join(cumul,lis[i])
                #print(cumul)
        interrupt(lis)
        if analyze:
            print("To create in target: " + filetocreate)
        else:
            try:
                print("Creating " + filetocreate + " ... ", end="", flush = True)
                shutil.copyfile(value, filetocreate)
                print("Done")
                interrupt()
            except:
                print("Exception raised but still running: " + e)
    # 4. Remove the potential void folders in target
    for root, dirs, files in os.walk(path):
        if len(os.listdir(root)) == 0:
            interrupt("Folder is void and will be suppressed: " + root)
            try:
                shutil.rmtree(root)
            except Exception as e:
                print("The folder " + root + "is not existing anymore so cannot be removed...")
                print("Exception raised but still running: " + e)


#============================================ usage
def usage():
    print("Synchronize 2 folders and their contents")
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
    dict = analyze_source(source)
    analyze_target(target, dict, analyzemode)

    
if __name__ == "__main__":
    main()
        
        
        


        
