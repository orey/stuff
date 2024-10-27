import sys, argparse, os
from rdflib import Graph, Literal, URIRef, RDF, RDFS, XSD

# local imports
sys.path.append(".")
from tools import interrupt, generate_name



#SOURCE = "/home/olivier/Documents/gedcom/20240402landry.ged"
#TARGETDIR = "/home/olivier/Documents/gedcom/"
#TARGETNAME = "20240402landry.ttl"
#TARGETGML = "20240402landry.gml"

DOMAIN = "https://n.org/rdf/v01/"




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
        print(str(len(leveltags[i])) + " tags of level " + str(i) + ": ", end = "")
        print(leveltags[i])
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
                tokens = line.strip().split(" ")
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
                        currentid = tokens[1].split("@")[1].strip()
                    else:
                        print("WTF: " + tokens[1])
                        sys.exit()
                    currentchunk = []
            else:
                if not headerfinished:
                    header.append(line.strip())
                else:
                    currentchunk.append(line.strip())
        print("We should never arrive here")

        
#================================================= format_URI
def format_URI(domain, pred):
    new = ''
    for i, c in enumerate(pred):
        if c in [' ', '-', '/', '\\', '(',')',',',
                 '"', "'", "<", ">", "|", "{", "}",
                 "^", "#", "$", "*", ".", "`", "+",
                 "=", "%"]:
            new += '_'
        else:
            new += pred[i]
    new = new.strip()
    return URIRef(domain + new)


#I1193020731
#['1 NAME Morgane Michèle Rose /REY/\n', '2 SURN REY\n', '2 GIVN Morgane Michèle Rose\n', '1 SEX F\n', '1 BIRT\n', "2 PLAC Aix-en-Provence, Bouches-du-Rhône, Provence-Alpes-Côte d'Azur, France, , , \n", '2 DATE 7 AUG 2012\n', '1 FAMC @F464019274@\n']
#================================================= create Objects
def create_object(g, domain, id, chunk, verbose = False):
    mytype = ""
    if id.startswith("I"):
        if verbose: print("I",end="|")
        g.add((
            format_URI(DOMAIN, id),
            RDF.type,
            format_URI(DOMAIN, "INDI")
        ))
        for line in chunk:
            tokens = line.split(" ")
            if tokens[1] == "NAME":
                name = line[7:].replace('/', '').replace('"','').strip()
                g.add((
                    format_URI(DOMAIN, id),
                    format_URI(DOMAIN, "NAME"),
                    Literal(name)
                ))
#            elif tokens[1] == "FAMS":
#                famid = tokens[-1].replace('@','').strip()
#                g.add((
#                    format_URI(DOMAIN, id),
#                    format_URI(DOMAIN, "CHILD_OF"),
#                    format_URI(DOMAIN, famid)
#                ))            
#            elif tokens[1] == "FAMC":
#                famid = tokens[-1].replace('@','').strip()
#                g.add((
#                    format_URI(DOMAIN, id),
#                    format_URI(DOMAIN, "HUSBAND_OR_WIFE"),
#                    format_URI(DOMAIN, famid)
#                ))            
            else:
                #to be implemented
                continue
    elif id.startswith("F"):
        if verbose: print("F",end="|")
        mytype = "FAMILY"
        g.add((
            format_URI(DOMAIN, id),
            RDF.type,
            format_URI(DOMAIN, mytype)
        ))
        for line in chunk:
            tokens = line.split(" ")
            if tokens[1] in ["HUSB", "WIFE", "CHIL"]:
                theid = tokens[-1].replace('@', '')
                g.add((
                    format_URI(DOMAIN, id),
                    format_URI(DOMAIN, tokens[1]),
                    format_URI(DOMAIN, theid)
                ))        
            else:
                #to be implemented
                continue
    else:
        mytype ="TO_BE_TYPED"

        
#================================================= parse families
def parse_individuals(chunks):
    mydict = {} #{id1: name1, id2:name2, ...}
    for id in chunks:
        if id.startswith("I"):
            chunk = chunks[id]
            name = ""
            for line in chunk:
                tokens = line.split(" ")
                if tokens[1] == "NAME":
                    if len(line) < 8:
                        name = id
                    else:
                        name = line[7:].replace('/', '').replace('"','').strip()
                    if id in mydict:
                        print("Strange: " + id + " already in dict")
                        continue
                    else:
                        mydict[id] = name
    return mydict
                    

def gmlid(id):
    #return str(int(id.replace("I","")))
    return id.replace("I","")

            
#================================================= parse families
def parse_families(g, chunks, names):
    mydict = {} #{indi1:{"FATH" : indi2father, "MOTH" : indi3Mother, "HUSB" : indi4, "WIFE": indi4}, ... }
    count = 0
    gml = ['graph [\n']
    for e in names:
        gml.append('node [\n  id ' + gmlid(e) + '\n  label "' + names[e] + '"\n]\n')
    for id in chunks:
        if id.startswith("F"):
            count += 1
            chunk = chunks[id]
            #analyzing family
            husb = ""
            wife = ""
            children = []
            for line in chunk:
                tokens = line.split(" ")
                if tokens[1] == "HUSB" and len(tokens) > 2:
                    husb = tokens[2].replace('@','').strip()
                elif tokens[1] == "WIFE" and len(tokens) > 2:
                    wife = tokens[2].replace('@','').strip()
                elif tokens[1] == "CHIL" and len(tokens) > 2:
                    children.append(tokens[2].replace('@','').strip())
                else:
                    continue
            if husb != '' and wife != '':
                g.add((
                    format_URI(DOMAIN, names[husb]),
                    format_URI(DOMAIN, "husb-wife"),
                    format_URI(DOMAIN, names[wife])
                ))
                gml.append('edge [\n  label "' + "husb-wife" + '"\n'
                           + '  source ' + gmlid(husb) + '\n  target ' + gmlid(wife) + '\n]\n')
            for child in children:
                if child != '' and husb != '':
                    g.add((
                        format_URI(DOMAIN, names[husb]),
                        format_URI(DOMAIN, "father"),
                        format_URI(DOMAIN, names[child])
                    ))
                    gml.append('edge [\n  label "' + "father" + '"\n'
                           + '  source ' + gmlid(husb) + '\n  target '+ gmlid(child) + '\n]\n')
                if child != '' and wife != '':
                    g.add((
                        format_URI(DOMAIN, names[wife]),
                        format_URI(DOMAIN, "mother"),
                        format_URI(DOMAIN, names[child])
                    ))
                    gml.append('edge [\n  label "' + "mother" + '"\n'
                           + '  source ' + gmlid(wife) + '\n  target '+ gmlid(child) + '\n]\n')
    gml.append(']\n')
    return count, gml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("SOURCE", help="The GED file with its path")
    parser.add_argument("TARGETDIR", help="Target directory to generate file(s)")
    parser.add_argument("--RDF", help="Option: generates a ttl file also (on top on the gml file)")
    args = parser.parse_args()
    SOURCE = args.SOURCE
    #test if that works under windows
    path_elems = os.path.normpath(SOURCE).split(os.sep)
    rootname = path_elems[-1].split(".")[0]
    TARGETDIR = args.TARGETDIR
    TARGETNAME = rootname + ".ttl"
    TARGETGML = rootname + ".gml"
    
    g = Graph()
    print("Analyzing " + SOURCE)
    analyze(SOURCE)
    print("Chunking " + SOURCE)    
    header, chunks = chunker(SOURCE)
    #for e in chunks:
    #    print(e, end="|")
    #print("\n")
    #id = "I1193020731"
    #print("ID = " + id)
    #print(chunks[id])
    #for id in chunks:
    #    create_object(g, DOMAIN, id, chunks[id], True)
    #print("")
    individuals = parse_individuals(chunks)
    print("Found " + str(len(individuals)) + " individuals in file " + SOURCE)
    count, gml = parse_families(g, chunks, individuals)
    print("Found " + str(count) + " families in file " + SOURCE)

    if args.RDF:
        output = TARGETDIR + generate_name(TARGETNAME)
        g.serialize(output, format='turtle')
        print("Turtle file " + output + " generated")
    
    outputgml = TARGETDIR + generate_name(TARGETGML)
    with open(outputgml, "w") as f:
        for line in gml:
            f.write(line)
    print("GML file " + outputgml + " generated")
    

if __name__ == '__main__':
    main()


