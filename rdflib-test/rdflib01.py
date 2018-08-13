import rdflib
from graphviz import Digraph,Graph

g = rdflib.Graph()
result = g.parse("http://www.w3.org/People/Berners-Lee/card")

print("graph has %s statements." % len(g))
# prints graph has 79 statements.

for subj, pred, obj in g:
   if (subj, pred, obj) not in g:
       raise Exception("It better be!")

s = g.serialize(format='n3')

#dot = Digraph()
dot = Graph()

print(s)

print("--- generating graphviz diagram ---")
ns = 0
no = 0
for s, p, o in g:
    print(s)
    #dot.edge(s.__str__(),o.__str__())
    #dot.edge(s.__str__(),o.__str__(),p.__str__())
#    first solution => display problem
#    print((s, p, o))
#    print("test : ", s.__str__())
#    n = dot.node("s"+str(ns),s.__str__())
#    print(n)
#    dot.node("o"+str(no),o.__str__())
#    dot.edge("s"+str(ns),"o"+str(no),p.__str__())
#    ns+=1
#    no+=1

print(dot.source)
#dot.render('test.gv', view=True)
#dot.format('png')
dot.view()    
