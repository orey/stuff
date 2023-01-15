import os, sys, getopt
import shutil
import hashlib
from time import time

VERBOSE=False

# key, fullpathtofile for all reference files
DICT_REF = {}

# key, fullpathtofile for all possible duplicate files
DICT_TEMP = {}

EXT='jpg'

path_ref =r'/home/olivier/olivier1/Pictures/'

path_temp=r'/home/olivier/olivier1/Recup-Crash-PC/'
#path_temp=r'/home/olivier/olivier1/Recup-Crash-PC/recup 20190721-2/'

# Test folders
#path_ref=r'/home/olivier/olivier1/folder-ref/'
#path_temp=r'/home/olivier/olivier1/folder-temp/'


def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()


def garbage(filename):
    # create garbage
    garb = os.path.join(os.getcwd(), "garbage")
    if not os.path.isdir(garb):
        os.mkdir(garb)
    timestamp = str(time()).split('.')[0] + str(time()).split('.')[1]
    #get just filename
    fil = filename.split('/')[-1]
    try:
        os.rename(filename, os.path.join(garb, timestamp + '-' + fil))
    except Exception as err:
        print(err)
        


def move_duplicate(rootpath, key, filename):
    temp = os.path.join(rootpath, key)
    if os.path.isdir(temp):
        print("Folder already exists")
    else:
        os.mkdir(temp)
    timestamp = str(time()).split('.')[0] + str(time()).split('.')[1]
    fil = filename.split('/')[-1]
    try:
        os.rename(filename, os.path.join(temp, timestamp + '-' + fil))
    except Exception as err:
        print(err)


    
# This function analyzes or moves the duplicates
def analyze_folder(extension, path, thedict, move=False):
    count = 0
    mykey = str(int(time()))
    if not move:
        # create logfile - move = False
        logfilename = mykey + '.html'
        logfile = open(logfilename, "w")
        logfile.write(format_header())
    else:
        # create folder for dupes - move = True
        rootpath = os.path.join(os.getcwd(), mykey)
        os.mkdir(rootpath)
    # main loop
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension) or file.endswith(extension.upper()):
                filename = os.path.join(root,file)
                sha = sha256sum(filename)
                #print(sha + " - " + filename)
                sys.stdout.write(str(count) + '|')
                sys.stdout.flush()
                count +=1
                if sha in thedict.keys():
                    print("\nFound duplicate: " + filename + " | " + thedict[sha])
                    if move:
                        move_duplicate(rootpath, sha, filename)
                    else:
                        logfile.write(format_line(filename, thedict[sha]))
                else:
                    thedict[sha] = filename
    if not move:
        logfile.write(format_trailer())
        logfile.close()


def format_header():
    return "<html>\n<body>\n"


def format_line(temp, real):
    return '<p><a href="file://' + temp + '">' + temp \
        + '</a> - <a href="file://' + real + '">' + real + '</a></p>\n'


def format_trailer():
    return "</body>\n</html>\n"


def compare_folders():
    #Analyse reference folder
    todelete = open("todelete.html", "w")
    tokeep   = open("tokeep.html"  , "w")
    todelete.write(format_header())
    tokeep.write(format_header())
    analyze_folder(EXT,path_ref,DICT_REF)
    analyze_folder(EXT,path_temp,DICT_TEMP)
    REF_KEYS = DICT_REF.keys()
    for key in DICT_TEMP.keys():
        if key in REF_KEYS:
            print("Duplicate: " + DICT_TEMP[key] + " - " +  DICT_REF[key])
            print("Moving file to the 'to-delete' location")
            todelete.write(format_line(DICT_TEMP[key],DICT_REF[key]))
            shutil.move(DICT_TEMP[key], r'/home/olivier/olivier1/to-delete/')
        else:
            print("Moving file to the 'to-keep' location")
            shutil.move(DICT_TEMP[key], r'/home/olivier/olivier1/to-keep/')
            tokeep.write(format_line(DICT_TEMP[key], " None"))

    todelete.write(format_trailer())
    todelete.close()
    tokeep.write(format_trailer())
    tokeep.close()


def usage():
    print("remove-dupes.py")
    print("Usage:")
    print("> python(3) remove-dupes.py -d")
    print("Analyses duplicates in a single folder")
    print("> python(3) remove-dupes.py -a")
    print("Analyses duplicates in two folders")
    sys.exit(2)

def main():
    if len(sys.argv) == 1:
        usage()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ad:v", ["all", "dir"])
    except getopt.GetoptError as err:
        usage()
    for o, a in opts:
        if o == "-v":
            VERBOSE = True
        elif o in ("-h", "--help"):
            usage()
        elif o in ("-a", "--all"):
            compare_folders()
        elif o in ("-d", "--dir"):
            analyze_folder(EXT,path_ref,DICT_REF)
            #test = input("Enter a char: ")
            #analyze_folder(EXT,path_temp,DICT_TEMP,True)
        else:
            assert False, "unhandled option"



if __name__ == "__main__":
    main()
    
