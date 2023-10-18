import os
import csv
 
# Get the list of all files and directories
path = "."
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)

def countLines(f, unicode=True, sep=','):
    nb = 0
    if unicode:
        with open(f,encoding = 'utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=sep)
            for line in spamreader:
                nb = nb + 1
    else:
        with open(f) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=sep)
            for line in spamreader:
                nb = nb + 1
    print("Number of records in " + f + ": " + str(nb))
    return nb

num = 0
for f in dir_list:
    if f.endswith(".csv"):
        print("Treating " + f)
        try:
            num = num + countLines(f, True, ',') #unicode mode
        except:
            num = num + countLines(f, False, ',')
print("===== Total number of lines: " + str(num))
