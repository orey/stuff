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

IMAGES_EXT = ["png", "jpg", "jpeg"]

def get_valid_folder(mystr):
    ok = false
    while (not ok):
        indir = input(mystr)
        if os.path.isdir(indir):
            return indir
        else:
            print("Folder is not valid.")

def get_valid_file(mystr):
    ok = false
    while (not ok):
        infile = input(mystr)
        if os.path.isfile(infile):
            return infile
        else:
            print("File is not valid.")


def parsefilename(fname):
    '''
    Returns year month day
    '''
    filename, file_extension = os.path.splitext(fname)
    return filename[0:4],filename[4:6],filename[6:8], filename + "." + file_extension

YEAR_HEADER = Template("# Année $year\n\n")
YEAR_MONTH  = Template("## Month $month\n\n")

IMAGE = Template("![image]($image)\n\n")

MONTH_HEADER = Template("# Mois $month $year\n\n")
MONTH_DAY    = Template("## Day $day\n\n")

DAY_HEADER = Template("# Jour $day $month $year\n\n")

def generate_summary_page(indir, outdir):
    onlyimages = []
    for f in listdir(indir):
        filename, file_extension = os.path.splitext(f)
        if (isfile(f) and file_extension in IMAGES_EXT):
            onlyimages.append(f)
    onlyimages.sort()
    currentyear  = ""
    currentmonth = ""
    currentday   = ""
    for f in onlyimages:
        theyear, themonth, theday, theimage = parsefilename(f)
        yearfile = monthfile = dayfile = None
        if (currentyear == ""):
            currentyear = theyear
            yearfile = open(os.path.join(outdir, theyear + ".md"), "w")
            yearfile.writeln(YEAR_HEADER.substitute(year=theyear))
        if (currentmont == ""):
            monthfile = themonth
            monthfile = open(os.path.join(outdir, theyear + themonth + ".md"), "w")
            monthfile.writeln(MONTH_HEADER.substitute(month=themonth,year=theyear))
            yearfile.writeln(MONTH_HEADER.substitute(month=themonth,year=theyear))
        if ((currentmonth != "") and (themonth != currentmonth)):
            currentmonth = themonth
            
        if (currentday == ""):
            dayfile = theday
            dayfile = open(os.path.join(outdir, theyear + themonth + theday + ".md"), "w")
            dayfile.writeln(DAY_HEADER.substitute(day=theday,month=themonth,year=theyear))
        yearfile.writeline(IMAGE.substitute(image=theimage))
        
            
            
        







    
def generate_day_pages(infile, indir, outdir):
            
if __name__ == "__main__":
    indir = get_valid_folder("Input the folder where the images are located: ")
    outdir = get_valid_folder("Input an output folder for the generated files: ")

    generate_summary_page(indir, outdir)
    generate_day_pages(indir, outdir)



    
