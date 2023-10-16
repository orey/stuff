import sys
import csv

#repos
ARC = "arc.csv"
COC = "coc.csv"

Arc = dict()
Coc = dict()

Accesses = []

def getName(s):
    return s.split('/')[-1]

# fil is the filename
# dic is the dictionnary
# appcol is a string with app
# rowidcol
# rowfilecol
def loadDict(fil, dic, idcol, filecol):
    # Creation of dictionnaries for ARC and COC
    print("==== LOADING DICTIONNARIES ====")
    with open(fil ,encoding = 'utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        count=0
        for row in spamreader:
            count =count+1
            if row[idcol] in dic:
                print("D|",end='', flush=True) #duplicate
            else:
                dic[row[idcol]] = getName(row[filecol])
                print("N|",end='', flush=True) #new

        #print(dic)
        print("")
        print("Number of records in dictionary: " + str(len(dic)))

        
class LogRecord:
    def __init__(self, app, user, filename, mydate):
        self.app = app
        self.user = user
        self.filename = filename
        self.date = mydate
    def print(self):
        print(self.app + " - " + self.user + " - " + self.filename + " - " + self.date)
    def getRow(self):
        return [self.app, self.user, self.filename, self.date]
            

def analyzeFile(app, fil, usercol, filenamecol, datecol, dict, separator=","):
    print("==== LOADING " + fil + " ====")
    with open(fil ,encoding = 'utf-8') as csvfile:
    #with open(fil) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=separator)
        num = 0
        for row in spamreader:
            if getName(row[filenamecol]) in dict.values():
                num = num + 1
                Accesses.append(LogRecord(app,row[usercol],row[filenamecol],row[datecol]))
                print(str(num) + "|", end='', flush=True)
                
        print("")

        
def generateOutput(fil):
    with open(fil, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Application", "User", "Filename", "Date"])
        for elem in Accesses:
            writer.writerow(elem.getRow())

            
if __name__ == '__main__':
    if len(sys.argv) != 7:
        print("Usage: python arc.py app filename usercol filenamecol datecol separator")
        sys.exit(0)
        
    app = sys.argv[1]
    filename = sys.argv[2]
    usercol = sys.argv[3]
    filenamecol = sys.argv[4]
    datecol = sys.argv[5]
    sep = sys.argv[6]
    
    print("filename: " + filename + " - usercol: " + usercol + " - filenamecol: " + filenamecol + " - datecol: " + datecol)

    print("Loading ARC dictionary")
    loadDict(ARC, Arc, 2, 6)
    print("Loading COC dictionary")
    loadDict(COC, Coc, 2, 6)

    if app == "ARC":
        print("Analyzing ARC accesses...")
        analyzeFile(app, filename, int(usercol), int(filenamecol), int(datecol), Arc, sep)
    else:
        print("Analyzing COC accesses...")
        analyzeFile(app, filename, int(usercol), int(filenamecol), int(datecol), Coc, sep)

    print("Found " + str(len(Accesses)) + " records of accesses")
    generateOutput('output-'+filename)
    print("output-" + app + "-" + filename + " was generated")



    



