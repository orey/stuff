import os, sys, shutil
import hashlib
from time import time
from datetime import datetime

GARBAGE = '/tmp/filesync_'
TIMESTAMP = datetime.now().strftime('%Y%m%d__%H%M%S-%f')


#============================================ interrupt
def interrupt(text):
    '''
    Manual breakpoint
    '''
    print(text)
    resp = input("Continue? ")
    if resp.upper() in ["N","NO"]:
        print("Goodbye!")
        exit(0)


# Unique footprint of the file
def sha256sum(completefilename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(completefilename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()


def ensure_folder(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)

        
# Garbaging file is just moving it for safety
def garbage(filename):
    garb = GARBAGE + TIMESTAMP
    if not os.path.isdir(garb):
        os.mkdir(garb)
        print(garb + " created")
    timestamp = str(time()).split('.')[0] + str(time()).split('.')[1]
    #get just filename
    fil = filename.split('/')[-1]
    try:
        shutil.move(filename, os.path.join(garb, timestamp + '-' + fil))
    except Exception as err:
        print(err)


# returns an dict       
def analyze_source(path):
    #creating a dict with key = relativepath/filename.ext : value = full path
    dict = {}
    count = 0
    for root, dirs, files in os.walk(path):
        print(dirs)
        for thefile in files: 
            count +=1
            # calculating the value
            completefilename = os.path.join(root,thefile)
            relativefilename = completefilename.split(path)[1]
            dict[relativefilename]=completefilename
            #interrupt(dict)
            sys.stdout.write(str(count) + '|')
            sys.stdout.flush()
    print("\n--- " + str(count) + " files found")
    return dict


def analyze_target(path, sourcedict):
    count = 0
    for root, dirs, files in os.walk(path):
        print(dirs)
        for thefile in files: 
            count +=1
            completefilename = os.path.join(root,thefile)
            relativefilename = completefilename.split(path)[1]
            # the objective is to see if this file is already at the "same" place in
            # the local folder
            try:
                completesourcefilename = sourcedict[relativefilename]
                print("Same file at the same place: " + relativefilename)
                interrupt(completesourcefilename)
                # Remove from sourcedict
                del sourcedict[relativefilename]
            except KeyError:
                print(sys.exception())
                print("File exists in remote but no more locally. Putting the file in the garbage.")
                garbage(completefilename)
                interrupt("File garbaged: " + completefilename)
    for key,value in sourcedict.items():
        filetocreate = os.path.join(path,key)
        interrupt("File to create: " + filetocreate)
        # check if folders exist
        lis = key.replace(key.split('/')[-1], "").split('/')
        if len(lis) > 1:
            cumul = path
            for i in range(0, len(lis)-1):
                ensure_folder(os.path.join(cumul,lis[i]))
                cumul = os.path.join(cumul,lis[i])
                print(cumul)
        interrupt(lis)
        
        shutil.copyfile(value, filetocreate)
        interrupt("Voir les drives")

                      
                
    




        
def main():
    local = "/home/olivier/JDR-RPG/JDR/Ambre/"
    remote = "/run/user/1000/gvfs/ftp:host=ls-wxl271.local/array1/DisqueBuffaloRaid1/JDR-RPG/JDR/Ambre/"
    dict = analyze_source(local)
    analyze_target(remote, dict)

    

    
if __name__ == "__main__":
    main()
        
        
        


        
