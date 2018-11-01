from rdflib import Graph, Literal, BNode, RDF
from rdflib.namespace import FOAF, DC
from graphviz import Digraph


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
#ns = 0
#no = 0
#for s, p, o in g:
#    print(s)
#    print((s, p, o))
#    print("test : ", s.__str__())
#    n = dot.node("s"+str(ns),s.__str__())
#    print(n)
#    dot.node("o"+str(no),o.__str__())
#    dot.edge("s"+str(ns),"o"+str(no),p.__str__())
#    ns+=1
#    no+=1

#print(dot.source)
#dot.render('test.gv', view=True)
#dot.format('png')
#dot.view()
