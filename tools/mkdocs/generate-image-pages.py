#---------------------------------------
# generate-image-pages.py
# Author: O. Rey
# Date: August 2020
# Licence: GPL V3
#---------------------------------------
#!/bin/python3
import os, sys
from os import listdir
from os.path import isfile, join
from string import Template
import configparser

#----------------------------------------
IMAGES_EXT = [".png", ".jpg", ".jpeg"]


#----------------------------------------
def get_valid_folder(mystr):
    ok = False
    while (not ok):
        indir = input(mystr)
        if os.path.isdir(indir):
            print(indir)
            return indir
        else:
            print("Folder is not valid.")

            
#----------------------------------------
def get_valid_file(mystr):
    ok = False
    while (not ok):
        infile = input(mystr)
        if os.path.isfile(infile):
            print(indir)
            return infile
        else:
            print("File is not valid.")


#----------------------------------------
def parsefilename(fname):
    '''
    Returns year month day
    '''
    filename, file_extension = os.path.splitext(fname)
    titre = filename[23:]
    if titre == "":
        print("Info: cannot retrieve title of meeting.")
        titre = "Meeting"
    return filename[0:4],filename[4:6],filename[6:8], titre


#----------------------------------------
YEAR_HEADER = Template("# YEAR $year\n\n")
YEAR_MONTH  = Template("* Month $month: [$year$month]($year$month.md)\n")

MONTH_HEADER = Template("# MONTH $month $year\n\n")
MONTH_DAY    = Template("* Day $day: [$year$month$day]($year$month$day.md)\n")

DAY_HEADER = Template("# DAY $day $month $year\n\n")

IMAGE = Template("![$titre]($image)\n\n")

#----------------------------------------
def generate_pages(indir, outdir, relpath):
    onlyimages = []
    for f in listdir(indir):
        filename, file_extension = os.path.splitext(f)
        print(filename + " | " + file_extension)
        if (file_extension in IMAGES_EXT):
            onlyimages.append(f)
            print(f)
    onlyimages.sort()
    currentyear  = ""
    currentmonth = ""
    currentday   = ""
    yearfile = None
    monthfile = None
    dayfile = None
    for f in onlyimages:
        theyear, themonth, theday, thetitle = parsefilename(f)
        print(f)
        if (currentyear == ""):
            # First image will provide the year for the other lines
            currentyear = theyear
            yearfile = open(os.path.join(outdir, theyear + ".md"), "w")

            print(">>> file " + os.path.join(outdir, theyear + ".md") + " opened")
            # a = input("pause")
            
            print(os.path.join(outdir, theyear + ".md"))
            yearfile.write(YEAR_HEADER.substitute(year=theyear))
        if (currentmonth == ""):
            # First time we create the month both in the year file and in the month file
            currentmonth = themonth
            monthfile = open(os.path.join(outdir, theyear + themonth + ".md"), "w")

            print(">>> file " + os.path.join(outdir, theyear + themonth + ".md") + " opened")
            # a = input("pause")
            
            monthfile.write(MONTH_HEADER.substitute(month=themonth,year=theyear))
            yearfile.write(YEAR_MONTH.substitute(month=themonth,year=theyear))
        if ((currentmonth != "") and (themonth != currentmonth)):
            # Change on month
            currentmonth = themonth
            monthfile.close()
            monthfile = open(os.path.join(outdir, theyear + themonth + ".md"), "w")

            print(">>> file " + os.path.join(outdir, theyear + themonth + ".md") + "opened")
            # a = input("pause")

            monthfile.write(MONTH_HEADER.substitute(month=themonth,year=theyear))
            yearfile.write(YEAR_MONTH.substitute(month=themonth,year=theyear))
        if (currentday == ""):
            # first day
            currentday = theday
            dayfile = open(os.path.join(outdir, theyear + themonth + theday + ".md"), "w")

            print(">>> file " + os.path.join(outdir, theyear + themonth + theday+ ".md") + " opened")
            # a = input("pause")

            dayfile.write(DAY_HEADER.substitute(day=theday,month=themonth,year=theyear))
            monthfile.write(MONTH_DAY.substitute(day=theday,month=themonth,year=theyear))
        if ((currentday != "") and (theday != currentday)):
            currentday = theday
            if dayfile != None:
                dayfile.close()
            dayfile = open(os.path.join(outdir, theyear + themonth + theday + ".md"), "w")

            print(">>> file " + os.path.join(outdir, theyear + themonth + theday+ ".md") + " opened")
            # a = input("pause")

            dayfile.write(DAY_HEADER.substitute(day=theday,month=themonth,year=theyear))
            if monthfile != None:
                monthfile.write(MONTH_DAY.substitute(day=theday,month=themonth,year=theyear))
            else:
                print("Strange case: month file not opened => " + themonth)
        #yearfile.write(IMAGE.substitute(image=relpath+f))
        #monthfile.write(IMAGE.substitute(image=relpath+f))
        dayfile.write(IMAGE.substitute(image=relpath+f, titre=thetitle))

        
#----------------------------------------
SECTION = 'CONFIG'
INDIR   = 'ImageFolderPath'
OUTDIR  = 'GeneratedFilePath'
# Should have a / at the end
RELPATH = 'RelativePath'


#----------------------------------------
if __name__ == "__main__":
    # indir = get_valid_folder("Input the folder where the images are located: ")
    # outdir = get_valid_folder("Input an output folder for the generated files: ")
    # relpath = input("Provide the relative path of images with / at the end: ")

    config = configparser.ConfigParser()
    config.read("config.ini")
    indir = config[SECTION][INDIR]
    if not os.path.isdir(indir):
        print(INDIR + " is not a folder:")
        print(indir)
        print("Exiting...")
        sys.exit(0)
    outdir = config[SECTION][OUTDIR]
    if not os.path.isdir(outdir):
        print(OUTDIR + "is not a folder:")
        print(outdir)
        print("Exiting...")
        sys.exit(0)
    relpath = config[SECTION][RELPATH]
    if not relpath.endswith('/'):
        print("Warning, " + RELPATH + " variable should finish with a /. Completing.")
        relpath = relpath + '/'
        print(relpath)
    generate_pages(indir, outdir, relpath)



    
