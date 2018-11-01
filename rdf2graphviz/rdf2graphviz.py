import uuid, rdflib, sys, csv

from rdflib import Graph, Literal, BNode, RDF
from rdflib.namespace import FOAF, DC
from graphviz import Digraph

MAX_STRING_LENGTH = 40

def analyze_uri(uri):
    tokens = uri.split('/')
    if 'http:' in tokens or 'https:' in tokens:
        domain = tokens[2].split('.')[-2]
        mtype  = tokens[-1]
        return domain + ':' + mtype 
    else:
        print('Strange URI: ' + str(uri))
        return str(uri)


class RDFNode():
    def __init__(self, ident):
        self.id = uuid.uuid1()
        self.name = "void"
        if not isinstance(ident, rdflib.term.Identifier):
            raise TypeError("Unrecognized type: " + str(type(ident)))
        if type(ident) == rdflib.term.URIRef:
            self.name = analyze_uri(ident.toPython())
        elif type(ident) == rdflib.term.BNode \
          or type(ident) == rdflib.term.Literal:
            value = str(ident.toPython())
            if len(value) > MAX_STRING_LENGTH:
                self.name = value[0:MAX_STRING_LENGTH] + '...'
            else:
                self.name = value
        else:
            raise TypeError("Unrecognized type: " + str(type(ident)))
    def to_dot(self):
        return str(self.id), str(self.name)
    def get_name(self):
        return self.name
    def get_id(self):
        return str(self.id)

class RDFRel(RDFNode):
    def __init__(self, ident, source, target):
        RDFNode.__init__(self, ident)
        if type(source) != RDFNode:
            raise TypeError("Unrecognize type: " + str(type(source)))
        elif type(target) != RDFNode:
            raise TypeError("Unrecognize type: " + str(type(target)))
        self.source = source
        self.target = target
    def to_dot(self):
        return self.source.get_id(), self.target.get_id(), str(self.name)
    def get_source_id(self):
        return self.source.get_id()
    def get_target_id(self):
        return self.target.get_id()

def print_rel_as_box(rel, dot):
    dot.node(rel.get_id(),rel.get_name(), shape='box')
    dot.edge(rel.get_source_id(), rel.get_id())
    dot.edge(rel.get_id(), rel.get_target_id())
            

def add_to_nodes_dict(rdfnode, node_dict):
    '''
    We suppose that the parser will create an instance of node for each
    parse triple
    '''
    name = rdfnode.get_name()
    if name in node_dict:
        print("Info: same node won't be written in the dictionary")
        return node_dict[name]
    else:
        node_dict[name] = rdfnode
        return node_dict[name]
        
def add_to_rels_dict(rdfrel, rel_dict):
    '''
    We suppose that all relationships are unique, even if they have
    the same label
    '''
    rel_dict[rdfrel.get_id()] = rdfrel

def add_rdf_graph_to_dot(dot, rdfgraph, rel_as_labels = True):
    node_dict = {}
    rel_dict  = {}
    for s, p, o in rdfgraph:
        source = add_to_nodes_dict(RDFNode(s),node_dict)
        target = add_to_nodes_dict(RDFNode(o),node_dict)
        add_to_rels_dict(RDFRel(p, source, target),rel_dict)
    for elem in node_dict.values():
        dot.node(*elem.to_dot(), color="blue", fontcolor='blue')
    for elem in rel_dict.values():
        if rel_as_labels:
            dot.edge(*elem.to_dot())
        else:
            print_rel_as_box(elem, dot)
    return dot
    
def print_store(store):
    # Iterate over triples in store and print them out.
    print("--- printing raw triples ---")
    for s, p, o in store:
        print(s, p, o)
    
    # Serialize as XML
    print("--- start: rdf-xml ---")
    print(store.serialize(format="pretty-xml"))
    print("--- end: rdf-xml ---\n")

    # Serialize as Turtle
    print("--- start: turtle ---")
    print(store.serialize(format="turtle"))
    print("--- end: turtle ---\n")

    # Serialize as NTriples
    print("--- start: ntriples ---")
    print(store.serialize(format="nt"))
    print("--- end: ntriples ---\n")
    
def test1():
    store = Graph()

    # Bind a few prefix, namespace pairs for pretty output
    store.bind("dc", DC)
    store.bind("foaf", FOAF)

    # Create an identifier to use as the subject for Donna.
    donna = BNode()

    # Add triples using store's add method.
    store.add((donna, RDF.type, FOAF.Person))
    store.add((donna, FOAF.nick, Literal("donna", lang="foo")))
    store.add((donna, FOAF.name, Literal("Donna Fales")))
    
    print_store(store)
    
    # Dump store
    store.serialize("test1.rdf", format="pretty-xml", max_depth=3)
    
    dot = Digraph(comment='Test1')
    add_rdf_graph_to_dot(dot, store)
    dot.render('test1.dot', view=True)
    
def test2():
    store = Graph()
    result = store.parse("http://www.w3.org/People/Berners-Lee/card")
    print_store(store)

    # Dump store
    store.serialize("test2.rdf", format="turtle")
    
    dot = Digraph(comment='Test2')
    add_rdf_graph_to_dot(dot, store)
    dot.render('test2.dot', view=True)

def test3():
    store = Graph()
    result = store.parse("http://www.w3.org/People/Berners-Lee/card")
    print_store(store)

    # Dump store
    store.serialize("test3.rdf", format="turtle")
    
    dot = Digraph(comment='Test3')
    add_rdf_graph_to_dot(dot, store, False)
    dot.render('test3.dot', view=True)

class CI():
    def __init__(self, row):
        self.WBS = row[0]
        self.Doc_Type = row[1]
        self.Part_number = row[2]
        self.Issue = row[3]
        self.Father_parts = row[4]
        self.CI_before = row[5]
        self.Title = row[6]
        self.CI_type = row[7]
        self.Status = row[8]
        self.Creation_Date = row[9]
        self.Released_Date = row[10]
        self.Usage = row[11]
        self.CI_characteristic = row[12]
        self.Substitute = row[13]
        self.Des_group = row[14]
        self.MOE = row[15]
        self.SDU = row[16]
        self.APPLICABILITY = row[17]
        self.SMR = row[18]
        self.SAP = row[19]
        self.Conf = row[20]
        Tself.DE_below = row[21]
        self.ADU_Father = row[22]
        self.ECR = row[23]
        self.ECP = row[24]
        self.ECO_Fathers = row[25]
        self.ECO = row[26]
        self.ECO_links = row[27]
        self.NOT_ECO = row[28]
        self.Part_Effectivity_EC175_B = row[29]
        self.Part_Effectivity_Z15F = row[30]
        self.Part_Effectivity_Z15_Shipset = row[31]
        self.Part_Effectivity_EC175_B1 = row[32]
        self.EC175_B_from = row[33]
        self.EC175_B_to = row[34]
        self.EC175-B1_from = row[35]
        self.EC175-B1_to = row[36]
        self.Average_Weight = row[37]
        self.Weighed_Weight_1 = row[38]
        self.Weighed_Weight_2 = row[39]
        self.Weighed_Weight_3 = row[40]
        self.Weighed_Weight_4 = row[41]
        self.Weighed_Weight_5 = row[42]
        self.Weighed_Weight_6 = row[43]
        self.Weighed_Weight_7 = row[44]
        self.Weighed_Weight_8 = row[45]
        self.Weighed_Weight_9 = row[46]
        self.Weighed_Weight_10 = row[47]
        self.Weighed_Weight_11 = row[48]
        self.Weighed_Weight_12 = row[49]
        self.Weighed_Weight_13 = row[50]
        self.Weighed_Weight_14 = row[51]
        self.Weighed_Weight_15 = row[52]
        self.WB_Weight = row[53]
        self.Auto_Calculated_Weight = row[54]
        self.Calculated_Weight = row[55]
        self.Estimated_Weight = row[56]
        self.COG_X = row[57]
        self.COG_Y = row[58]
        self.COG_Z = row[59]
        self.Auto_Calculated_COG_X = row[60]
        self.Auto_Calculated_COG_Y = row[61]
        self.Auto_Calculated_COG_Z = row[62]
        self.WB_COG_X = row[63]
        self.WB_COG_Y = row[64]
        self.WB_COG_Z = row[65]




def test4(filename):
    reader = csv.reader(open(filename, "rb"), delimiter=';')
    i = 0
    # create target dict    dic = PriceList()
#    try:
#        for row in reader:
#            obj = OBJ(row)
#            add to target dict
#            i +=1
#        print("%d lines loaded" % (i-1))
#    except csv.Error as e:
#        print("Error caught in loading csv file")
#        print(e)

    
if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) != 2:
        test1()
        exit(1)
    a = sys.argv[1]
    if a == 1:
        test1()
    elif a == '2':
        test2()
    elif a == '3':
        test3()
    else:
        test1()
