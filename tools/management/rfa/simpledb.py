import json, os, shutil
from datetime import datetime
import os.path


OK = True
KO = False

NOT_FOUND = "Not found"
ABORT = -1

DATA = "data"
ID = "id"
TYPE = "type"
NAME = "name"
DESCR = "descr"

# Each type is a dict with 4 mandatory fields:
# id, type, name, descr

TEMPLATE = {"data":[{
    "id":0,
    "type":"__type__",
    "name":"__control__",
    "descr":"Fake description"
}]
}


def load_file(name):
    '''
    The structure of the db is by default the TEMPLATE
    '''
    with open(name, 'r') as f:
        data = json.load(f)
    # db is a list of objects
    return data

    
def create_file(name, content):
    '''
    This function encapsulates the output format (JSON)
    '''
    j = json.dumps(content)
    with open(name, 'w') as f:
        f.write(j)


def create_timestamp():
    '''
    This timestamp is useful for backups of the db
    '''
    temp = str(datetime.now())
    thedate = temp.split(" ")[0].replace('-', "")
    thetime = temp.split(" ")[1].replace(':', "")
    return thedate + "_" + thetime + "_"


def backup_file(filename):
    '''
    This function creates the backup file from a file
    '''
    fil = filename.split('/')[-1]
    new = filename.replace (fil, create_timestamp() + fil)
    try:
        shutil.copy(filename, new)
    except Exception as err:
        print(err)


class simpledb:
    '''
    The database
    '''
    def __init__(self, f, verbose=False):
        '''
        The only thing that the database manages is unicity
        of ids. id is int and is autoincremented.
        This base must be used in command line because it asks
        questions to the user.
        '''
        self.verbose = verbose
        if f == "" or f == None:
            print("Error: please provide a filename")
            return False
        # the file does not exist
        if not os.path.isfile(f):
            self.f = f
            self.root = TEMPLATE
            self.db = self.root[DATA]
            self.max = 0
            create_file(f, self.root)
            if verbose:
                print("Database created with no records in it")
            return
        # case where we open a file
        self.f = f
        backup_file(f)
        self.root = load_file(f)
        self.db = self.root[DATA]
        max = 0
        for elem in self.db:
            max = elem[ID] if elem[ID] > max else max
        self.max = max
        if verbose:
            print("Max " + ID + ": " + str(max))
        return

    def add_new(self, obj):
        id = self.max + 1
        obj[ID] = id
        self.db.append(obj)
        if self.verbose:
            print("New object recorded, " + ID + "=" + str(id))

    def update(self, obj):
        '''
        Updates the elem or add it
        '''
        id = obj.id
        theelem = None
        for i in range(len(self.db)):
            elem = self.db[i]
            if elem[id] == id:
                theelem = elem
                break
        if theelem == None:
            print("Warning: Object with " + ID + "=" + str(id) + "not found for update")
            print(elem)
            answer = input("Do you want to add it to the database? [y/n] ")
            if answer.upper() in ['Y', 'YES']:
                self.db.append(obj)
                return True
            else:
                print("Database not updated")
                return False
        else:
            del self.db[i]
            self.db.append(theelem)

    def search(pattern):
        acc = []
        for e in self.db:
            if pattern in e.name or pattern in e.descr:
                acc.append(e)
            if len(acc) == 0:
                return NOT_FOUND
            if len(acc) > 1:
                for elem in acc:
                    print("Several candidates found:")
                    print("[" + str(i) + "] ", end = "")
                    print(elem)
                print("[a] Abort")
                while True:
                    choice = input("Your choice? ")
                    if choice == "a":
                        return ABORT
                    try:
                        intchoice = int(choice)
                        return acc[intchoice]
                    except:
                        print("Choice not understood, try again")
            # In that case, there is only one
            return acc[0]

    def save(self):
        backup_file(self.f)
        create_file(self.f, self.root)
        

