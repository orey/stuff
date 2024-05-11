from html.parser import HTMLParser
import urllib.request
from urllib.parse import unquote
from string import Template
import os

# URLs
URL = "https://your-url/"
URLTEST = "https://your-test-url/"

#Output file
OUTPUT = "scanned-website.html"

# GRAMMAR
FOLDERS = "Folders"
TXT = "TXT"
PDF = "PDF"
MD = "MD"

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
        return [self.pdfs, self.folders]


def parseURL(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    #print(mystr)
    parser = MyHTMLParser(url)
    parser.feed(mystr)
    #parser.printPageContent()
    #parser.dumpArrays()
    return parser.getArrays()


def recursiveExplore(f, url, depth):
    print("Treating " + unquote(url))
    [pdfs, urlfolders] = parseURL(url)
    f.write('<h'+ str(depth) + '>Contents of ' + unquote(url) + '</h' + str(depth) + '><pre>\n')
    for pdf in pdfs:
        writeLink(f, pdf)
    f.write('</pre>\n')
    for urlfolder in urlfolders:
        recursiveExplore(f,urlfolder, depth+1)
    

def writeLink(f, linkurl):
    #print(linkurl)
    f.write('<a href="' + linkurl +'">' + unquote(linkurl.split('/')[-1]) + '</a>\n')
    
    
def writeHeader(f, myurl):
    str = Template("""
<html>
<head><title>Full Dump of $url</title></head>
<body bgcolor="white">
""")
    f.write(str.substitute(url = myurl))


def writeFooter(f):
    f.write("<hr>\n</body>\n</html>\n")

            
def main():
    #url = URLTEST
    url = URL
    with open(OUTPUT, "w") as f:
        writeHeader(f, url)
        recursiveExplore(f, url, 1)
        writeFooter(f)
    print("Dump done")

    
if __name__ == "__main__":
          main()

