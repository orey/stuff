#----------------------------------------
#-- Generator of classes for CSV files
#-- Author: O. Rey
#-- Copyleft 2018
#-- Under GPL V3 license
#----------------------------------------

import os.path, sys, getopt

VERBOSE = True

class Grammar:
    OPEN  = "{{"
    CLOSE = "}}"
    LOOPBEGIN = "LOOP"
    LOOPEND   = "LOOPEND"
    ELEM = "ELEM" # Loop element keyword
    TEMPLATE_EXT = ".template"

def checkTemplate(file):
    if not os.path.isfile(file):
        print("Error: " + file + " is not a valid file")
        sys.exit(0)
    else:
        if VERBOSE: print(file + " is a valid file")
    head, tail = os.path.split(file)
    if VERBOSE:
        print("head= " + head)
        print("tail= " + tail)
    if tail.endswith(Grammar.TEMPLATE_EXT): print("This is a template")
        
    

    

def main2():
    print("------------------------------------------------")
    checkTemplate("README.md")
    checkTemplate("../../README.md")
    checkTemplate("./templates/csvclass.py.template")
    checkTemplate("prout")
    print("------------------------------------------------")


def usage():
    print("Usage:")
    print("~$ python3 generator -f FILENAME")
    
def main():
    if len(sys.argv) == 1: usage()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvtf:", ["file"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)
        usage()
        sys.exit(2)
    filename = ""
    for o, a in opts:
        if o == "-v":
            VERBOSE = True
        # help option
        elif o in ("-h", "--help"):
            usage()
            return
        # File option - currently not implemented
        elif o in ("-f", "--file"):
            if ((a != None) or (a != "")):
                filename = a
                if VERBOSE:
                    print("filename: " + filename)
                main2()
                return
            else:
                print("No filename provided")
                usage()
                return
        elif o in ("-t", "--test"):
            #test(a)
            return
        else:
            print("Unhandled option: " + o)
            return
    

if __name__=="__main__":
    main()
