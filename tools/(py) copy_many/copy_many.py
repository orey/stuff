#------------------------------------------
# Massive copy from input file
#------------------------------------------
# Author : O. Rey
# License : GPL V3
# Date : May 2021
#------------------------------------------
#!/bin/python3
import sys, os, shutil, codecs, io

def usage():
    print("Usage: copy_many.py [file_with_list of files] [destination folder (with / in windows and / at the end)]")
    sys.exit(0);

def file_exists(line, odir):
    filename = os.path.basename(line)
    mycopy = os.path.join(odir, filename)
    return os.path.exists(mycopy)
    
    
if __name__ ==  "__main__":
    if len(sys.argv) != 3:
        usage()
    ifile = sys.argv[1].replace('\\', '/')
    print("Inbound file: " + str(ifile))
    odir = sys.argv[2].replace('\\', '/')
    print("Outbound dir: " + str(odir))
    if not os.path.isdir(odir):
        os.makedirs(odir)
    with io.open(ifile, 'r', encoding='utf8') as f:
        for line in f:
            line = line.replace('\\', '/')
            l = len(line)
            if line[-1] == '\n' and l > 1:
                line = line[0:l-1]
            if ".zip/" in line:
                # we must get the true file to copy wich is a zip file
                i = line.find(".zip")
                line = line[0:i+4]
            if ".7z/" in line:
                # we must get the true file to copy wich is a zip file
                i = line.find(".7z")
                line = line[0:i+3]
            if file_exists(line , odir):
                print("File already exists in target dir. Skipping...")
            else:
                print("Copying: " + line)
                try:
                    shutil.copy2(line, odir)
                except Exception as e:
                    print(e)
                    
