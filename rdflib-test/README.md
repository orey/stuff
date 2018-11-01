# rdflib-test

Test of python rdflib for various use cases

## Comments during development

Perspective: mapping web semantic concepts to
graphs.

Even to be able to display triples, we have to consider
that nodes have unique IDs but relationships must
be turn into instances.

Thus:
  * BNode instances and Literal instances should have
a unique ID
  * But the URIRef is more a type that should
be instanciated.

This transformation is required to display triples
as a graph form.