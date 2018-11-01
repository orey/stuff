import uuid, rdflib

from rdflib import Graph, Literal, BNode, RDF
from rdflib.namespace import FOAF, DC
from graphviz import Digraph


DISPLAY = { "http://xmlns.com/foaf/0.1/name" : "FOAF:name",
            "http://www.w3.org/1999/02/22-rdf-syntax-ns#type" : "RDF:type",
            "http://xmlns.com/foaf/0.1/nick" : "FOAF:nickname",
            "http://xmlns.com/foaf/0.1/Person" : "FOAF:Person"
}

NODES = {}
RELS = {}


class RDFNode():
    def __init__(self, ident):
        self.id = uuid.uuid1()
        self.name = "void"
        if not isinstance(ident, rdflib.term.Identifier):
            raise TypeError("Unrecognized type: " + str(type(ident)))
        if type(ident) == rdflib.term.URIRef:
            self.name = DISPLAY[ident.toPython()]
            if self.name == None:
                self.name = "UNKNOWN"
                print("Type not in grammar: " + ident.toPython())
        elif type(ident) == rdflib.term.BNode \
          or type(ident) == rdflib.term.Literal:
            self.name = ident.toPython()
        else:
            raise TypeError("Unrecognized type: " + str(type(ident)))
    def to_dot(self):
        return str(self.id), self.name
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
        return self.source.get_id(), self.target.get_id(), \
               self.name
#               'label="' + self.name + '"'

def add_to_nodes_dict(rdfnode):
    '''
    We suppose that the parser will create an instance of node for each
    parse triple
    '''
    name = rdfnode.get_name()
    if name in NODES:
        print("Info: same node won't be written in the dictionary")
        return NODES[name]
    else:
        NODES[name] = rdfnode
        return NODES[name]
        
def add_to_rels_dict(rdfrel):
    '''
    We suppose that all relationships are unique, even if they have
    the same label
    '''
    RELS[rdfrel.get_id()] = rdfrel



def get_id_display(thing):
    if type(thing) == rdflib.term.URIRef:
        display = DISPLAY[thing.toPython()]
        if display == None:
            print("Warning: " + thing.toPython() + " not in grammar")
            

if __name__ == '__main__':

    store = Graph()
    #result = g.parse("http://www.w3.org/People/Berners-Lee/card")


    # Bind a few prefix, namespace pairs for pretty output
    store.bind("dc", DC)
    store.bind("foaf", FOAF)

    # Create an identifier to use as the subject for Donna.
    donna = BNode()

    # Add triples using store's add method.
    store.add((donna, RDF.type, FOAF.Person))
    store.add((donna, FOAF.nick, Literal("donna", lang="foo")))
    store.add((donna, FOAF.name, Literal("Donna Fales")))

    # Iterate over triples in store and print them out.
    print("--- printing raw triples ---")
    for s, p, o in store:
        print(s, p, o)

    # For each foaf:Person in the store print out its mbox property.
    print("--- printing mboxes ---")
    for person in store.subjects(RDF.type, FOAF["Person"]):
        for mbox in store.objects(person, FOAF["mbox"]):
            print(mbox)

    print("graph has %s statements." % len(store))
    # Serialize the store as RDF/XML to the file donna_foaf.rdf.
    store.serialize("donna_foaf.rdf", format="pretty-xml", max_depth=3)

    # Let's show off the serializers

    print("RDF Serializations:")

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
    
    dot = Digraph(comment='RDF display')
    print("--- generating graphviz diagram ---")
    for s, p, o in store:
        print("--- Types ---")
        print("Type of s: ",type(s))
        print("Type of p: ",type(p))
        print("Type of o: ",type(o))
        print("--- toPython ---")
        print(s.toPython())
        print(p.toPython())
        print(o.toPython())
        print("--- storing to dot graph ---")
        source = add_to_nodes_dict(RDFNode(s))
        target = add_to_nodes_dict(RDFNode(o))
        add_to_rels_dict(RDFRel(p, source, target))
    
    print("--- generating graphviz diagram ---")
    for elem in NODES.values():
        dot.node(*elem.to_dot())
    for elem in RELS.values():
        dot.edge(*elem.to_dot())
    dot.render('test.gv', view=True)   
