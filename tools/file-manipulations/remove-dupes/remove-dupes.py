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
# move = 0 => analyze
# move = 1 => interactive
# move = 2 => automatic move
def analyze_folder(extension, path, thedict, move=0):
    count = 0
    duplicates = 0
    mykey = str(int(time()))
    if move == 0:
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
        for thefile in files:
            if thefile.endswith(extension) or thefile.endswith(extension.upper()):
                filename = os.path.join(root,thefile)
                sha = sha256sum(filename)
                #print(sha + " - " + filename)
                sys.stdout.write(str(count) + '|')
                sys.stdout.flush()
                count +=1
                if sha in thedict.keys():
                    print("\nFound duplicate: " + filename + " | " + thedict[sha])
                    duplicates +=1
                    if move == 2:
                        # automatic move
                        move_duplicate(rootpath, sha, filename)
                    elif move == 1:
                        print("Dir  1: " + os.path.dirname(filename) + '    <===>    ' + thefile)
                        print("Dir  2: " + os.path.dirname(thedict[sha]) + '    <===>    ' + os.path.basename(thedict[sha]))
                        choice = 0
                        while choice not in ["0","1","2"]:
                            sys.stdout.write("Type the file you want to keep, the other will be moved [1,2] or keep both [0]: ")
                            sys.stdout.flush()
                            choice = input()
                        if choice == "2":
                            # we keep the one in the dictionary
                            # we do as the automatic move
                            move_duplicate(rootpath, sha, filename)
                        elif choice == "1":
                            # we have to erase the one in the dictionary
                            # because other duplicates can come and we keep the one in the dict
                            move_duplicate(rootpath, sha, thedict[sha])
                            thedict[sha] = filename
                        else:
                            print("Both files kept")
                    else: # case where move = 0, analysis
                        logfile.write(format_line(thefile, os.path.dirname(filename), \
                                                  os.path.basename(thedict[sha]), os.path.dirname(thedict[sha])))
                        logfile.flush()
                else:
                    thedict[sha] = filename
    if not move:
        logfile.write(format_trailer())
        logfile.close()
    print("\nNumber of files analyzed: " + str(count))
    print("Number of duplicates found: " + str(duplicates))


def format_header():
    return "<html>\n<body><table>\n"


def format_line(filename, tempfolder, bisname, realfolder):
    return '<tr><td style="border: 1px solid black;">' + filename \
        + '</td><td style="border: 1px solid black;">' + tempfolder \
        + '</td><td style="border: 1px solid red;">' + bisname \
        + '</td><td style="border: 1px solid red;">' + realfolder \
        + '</td></tr>\n'


def format_trailer():
    return "</table></body>\n</html>\n"


# This function is old and must be reviewed before use
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
    print("> python(3) remove-dupes.py [ext] [folder] [analyze|interactive|move]")
    print("Analyses duplicates in a single folder or move them in a new folder created in the directory where the program is run.")
    print("Note: one exemplary (the first found) of the file is kept in the source folder, which can alter previous classification, especially if the files were renamed.")
    print("ext: extension, folder: surrounded by double quotes")
    sys.exit(2)

def main():
    if len(sys.argv) != 4:
        usage() #exits the program
    ext = sys.argv[1]
    print("Extension: " + ext)
    folder = sys.argv[2]
    print("Folder to process: " + folder)
    action = sys.argv[3]
    print("Action: " + action)
    # move = 0 => analyze
    # move = 1 => interactive
    # move = 2 => automatic move
    actionbin = 0
    if action == "move":
        sys.stdout.write("Are you sure you want to move all duplicated files? [Y,y]")
        sys.stdout.flush()
        test = input()
        if test in ["Y", "y"]:
            actionbin = 2
    elif action == "interactive":
        actionbin = 1
    else:
        actionbin = 0 #protects from rotten options
    #processing
    analyze_folder(ext,folder,DICT_REF, actionbin)


if __name__ == "__main__":
    main()
    
