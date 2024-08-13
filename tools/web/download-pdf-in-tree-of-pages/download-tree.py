import os, getopt, sys
from html.parser import HTMLParser
from urllib.parse import unquote
import urllib.request
from urllib.request import urlretrieve
from string import Template


# GRAMMAR
FOLDERS = "Folders"
TXT = "TXT"
PDF = "PDF"
MD = "MD"

#============================================ interrupt
def interrupt(str):
    '''
    Manual breakpoint
    '''
    print(str)
    resp = input("Continue? ")
    if resp.upper() in ["N","NO"]:
        print("Goodbye!")
        exit(0)

# One parser instance per page
class MyHTMLParser(HTMLParser):
    def __init__(self, baseurl):
        HTMLParser.__init__(self)
        self.baseurl = baseurl
        self.dict = {
            FOLDERS : 0,
            TXT : 0,
            MD  : 0,
            PDF : 0
        }
        self.folders = []
        self.pdfs = []
        
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            #print("Found a link. ", end = "")
            #search for href [('href', 'https://www.cwi.nl/')])
            if attrs[0][0] == 'href':
                value = attrs[0][1]
                #print(value)
                #print(attrs)
                if value.upper().endswith(TXT):
                    self.dict[TXT] += 1
                elif value.upper().endswith(MD):
                    self.dict[MD] += 1
                elif value.upper().endswith(PDF):
                    self.dict[PDF] += 1
                    self.pdfs.append(self.baseurl + value)
                elif value.endswith('/') and not value.endswith('../'):
                    self.dict[FOLDERS] += 1
                    self.folders.append(self.baseurl + value)

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        return

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        return

    def printPageContent(self):
        for elem in self.dict:
            print("Number of files of type " + elem + ": " + str(self.dict[elem]))

    def dumpArrays(self):
        print(self.pdfs)
        print(self.folders)

    def getArrays(self):
        return self.pdfs, self.folders


def parseURL(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    
    fp.close()
    parser = MyHTMLParser(url)
    parser.feed(mystr)
    #parser.printPageContent()
    #parser.dumpArrays()
    return parser.getArrays()


def recursiveDownload(basefolder,url, depth):
    print("Treating " + unquote(url))
    pdfs, urlfolders = parseURL(url)
    for pdf in pdfs:
        pdfname = pdf.split('/')[-1]
        print("Downloading: " + pdf)
        local_filename, headers = urlretrieve(pdf)
        pdffile = open(local_filename)
        pdffile.close()
        os.rename(local_filename,os.path.join(basefolder, unquote(pdfname)))
    for urlfolder in urlfolders:
        foldername = unquote(urlfolder.split('/')[-2])
        if not os.path.exists(os.path.join(basefolder,foldername)):
            os.makedirs(os.path.join(basefolder,foldername))
            print("=== Folder '" + str(os.path.join(basefolder,foldername)) + "' created")
        recursiveDownload(os.path.join(basefolder, foldername),urlfolder, depth+1)


def usage():
    print('Usage:\n> python download-tree.py -u "URL"')
    print("-URL must use % characters replacings specials (spaces, etc.) and be between double quotes")
    exit(0)

    
def main():
    # get options
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "-u:h",
                                   ["url=", "help"])
    except getopt.GetoptError:
        usage()

    URL = ""
    if len(sys.argv) == 1 or opts == []:
        usage()
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-u", "--url"):
            URL = a
            print("Root url: " + a)
        else:
            usage()

    #determine base folder
    basefolder = unquote(URL.split('/')[-2])
    if not os.path.exists(basefolder):
        os.makedirs(basefolder)
        print("=== Folder '" + basefolder + "' created")
    recursiveDownload(basefolder,URL, 1)
    print("All files retrieved. Exiting.")


if __name__ == "__main__":
    main()
