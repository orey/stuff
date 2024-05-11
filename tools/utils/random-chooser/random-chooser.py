import random
import json

FILENAME = 'list.json'

# Grammar
NAME ="name"
VERSION = "version"
LIST = "list"
CAT = "category"
SUB = "subcategory"
TEXT = "text"


def printHeader(dict):
    print("Name: " + dict[NAME])
    print("Version: " + dict[VERSION])

def printText(elem):
    print("-------------------------------")
    if CAT in elem:
        print("| Category    | " + elem[CAT])
    if SUB in elem:
        print("| Subcategory | " + elem[SUB])
    if TEXT in elem:
        print("| Text        | " + elem[TEXT])
    else:
        print("Strange, there should be a text in the element below...")
        print(elem)
    print("-------------------------------")

    
def main():
    with open(FILENAME) as f:
        dict = json.load(f)
        printHeader(dict)
        elems = dict[LIST]
        l = len(elems)
        print("Found " + str(l) + " elements in the list")
        resp = input("Are you ready? [y/n] ")
        reste = True
        if resp.upper() in ["Y","YES",""]:
            while reste:
                rank = random.choice(range(0,l))
                elem = elems[rank]
                printText(elem)
                del elems[rank]
                l = len(elems)
                if l == 0:
                    print("You've been through the full ist, bravo and goodbye!")
                    input("Press return to exit")
                    return
                print(str(l) + " elements remaining in the list")
                res = input("Continue? [y/n] ")
                if res.upper() not in ["Y","YES",""]:
                    reste = False
                    print("Goodbye !")

                
        


if __name__ == '__main__':
    main()
    
