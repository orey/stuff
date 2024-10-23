import sys, rdflib

# local imports
sys.path.append(".")
from tools import interrupt


SOURCE = "/home/olivier/Documents/gedcom/20240402landry.ged"




def analyze(sourcefile):
    # leveltags = [ { "TAG1" : nboftags1, "TAG2" = nboftags2, ...}, {...}, ...]
    # levels 0, 1, 2, 3, 4, 5
    leveltags = [{},{},{},{},{},{},{}]
    with open(sourcefile, "r") as f:
        slines = f.readlines()
        strange = []
        for roughline in slines:
            line = roughline.strip()
            tokens = line.split(" ")
            if tokens[0] == "0":
                if len(tokens) < 3:
                    strange.append(line)
                    continue
                else:
                    if not tokens[2] in leveltags[0]:
                        leveltags[0][tokens[2]] = 1
                        continue
                    else:
                        leveltags[0][tokens[2]] += 1
                        continue
            for i in range(1,6):
                if tokens[0] == str(i):
                    if not tokens[1] in leveltags[i]:
                        leveltags[i][tokens[1]] = 1
                        continue
                    else:
                        leveltags[i][tokens[1]] += 1
                        continue
            #this is the place for strange lines
            if tokens[0] not in ['0','1','2','3','4','5']:
                strange.append(line)
    print("Strange lines:") 
    print(strange)
    for i in range(6):
        print("Tags level " + str(i))
        print(leveltags[i])
        print("==> Nb of " + str(i) +"-level tags: " + str(len(leveltags[i])))
    return leveltags

def read_token(chunk):
    # first line is the level of the token
    count = 0
    roottoken = ""
    rootlevel = -1
    for line in chunk:
        if count == 0:
            tokens = line.split(" ")
            if tokens[1].startswith("@") and tokens[1].endswith("@"):
                roottoken = tokens[2]
    
                        
                    
def chunker(sourcefile):
    header = []
    chunks = {} # {id1: [line11, ...], id2:[line21, line22, ..], ...}
    headerfinished = False
    currenttoken = ""
    currentid = ""
    currentchunk = []
    with open(sourcefile, "r") as f:
        slines = f.readlines()
        for line in slines:
            if line.startswith("0 "):
                tokens = line.split(" ")
                if tokens[1].strip() == "TRLR":
                    print("End of file found")
                    #we have to write the last chunk
                    chunks[currentid] = currentchunk
                    return header, chunks
                #we have to write the previous chunk unless it is the first 0 token
                if not headerfinished:
                    headerfinished = True
                    currentid = tokens[1].split("@")[1]
                    currentchunk = []
                else:
                    # write the previous lines
                    chunks[currentid] = currentchunk
                    # general case: it is a new token
                    if tokens[1].startswith("@") and tokens[1].endswith("@"):
                        currentid = tokens[1].split("@")[1]
                    else:
                        print("WTF: " + tokens[1])
                        sys.exit()
                    currentchunk = []
            else:
                if not headerfinished:
                    header.append(line)
                else:
                    currentchunk.append(line)
        print("We should never arrive here")
        
            
            



def main():
    #g = Graph()
    analyze(SOURCE)
    header, chunks = chunker(SOURCE)
    for e in chunks:
        print(e, end="|")
    print("\n")
    id = "I1193020731"
    print("ID = " + id)
    print(chunks[id])


if __name__ == '__main__':
    main()


