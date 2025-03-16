import sys
sys.path.append('.')
from simpledb import simpledb

SUP = "supplier"
BUD = "budget"
PER = "person"
RFA = "rfa"
LIN = "link"

COM = [
    "sup",
    "bud",
    "per",
    "rfa",
    "lin"
]
MSG = [
    "Create a new supplier",
    "Create a new budget code",
    "Create a new person",
    "Create a new RFA",
    "Create a new nink"
]

RFA = {
    "id":-1,
    "type":"RFA",
    "name":"",
    "descr":"",
    "bud":""
}


# Prompt loop
def prompt():
    shell = ""
    while True:
        user_input = input("root > ")
        if not user_input in COM:
            print("Unrecognized command. Commands:")
            print(*COM)
            continue
        else:
            shell = user_input
        while True:
            shell_input = input(shell + " > ")
            
        

        command, *args = user_input.split(' ')
        args = args[0] if args else ''



def main():
    f = "db2.json"
    db = simpledb(f,True)
    print(db)
    db.save()
    prompt
    
    





if __name__ == "__main__":
    main()
