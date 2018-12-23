# Basic semantic graph transformations

This page is following [Basic graph transformations](basic-graph-transformations.md) but with a semantic graph perspective.

## Rich/poor level of information

A single triple is a "poor piece of information", but other triples with the same subjects can build a rich set of information.

Poor piece of information: `s p o .`

Rich piece of information:

```
s p o ;
  a S .
o a O .
```

## Time management

Rich piece of information: adding time information:

```
s p_23DEC2018 o ;
  a S .
o a O .
p_23DEC2018 a P .
P a Time_Predicate .
```

This is practical because `s P o .` can be deduced easily even if `s p_23DEC2018 o .` is more precise.

The statement `P a Time-Predicate .` indicates that P is a time-enabled predicate.

## Version management

We can have a variation of what we saw with version tagging.

```
s p_V2 o ;
  a S .
o a O .
p_V2 a P .
P a Version_Predicate .
```

## Managing life-cycle

Case of subject modification and history keeping.

Step 1. We have:

```
s1 p o .
```

Step 2: s1 becomes s2. We have:

```
s1 p o .
s2 previous s1 .
s2 p o . // "Rewiring"
```

This is ambiguous because the 3rd statement was made after the first. Let's use a time predicate.

```
s1 p_12DEC2018 o .
p_12DEC2018 a P .
P a Time_Predicate .
s2 previous s1 .
s2 p_23DEC2018 o . // "Rewiring"
p_23DEC2018 a P .
```

We can look at the graph at various moments.

Indeed, we still have:

```
s1 P o .
s2 previous s1 .
s2 P o . // "Rewiring"
```

But we also encoded a more precise information.

We could think about removing `s1 p o .` after `s2` is created but as the semantic web is a cumulative system, this does not seem very interesting.

## Shortcuts

Let's consider the pattern:

```
q = p<sub>1</sub> o p<sub>2</sub> o ... o p<sub>n</sub>
```

with `p<sub>i</sub>` a set of predicates.

```
s q a .
if
x<sub>n</sub> p<sub>n</sub> a .
and x<sub>n-1</sub> p<sub>-1</sub> x<sub>n</sub> .
and ..
and s p<sub>1</sub> x<sub>2</sub> . 
```

`q` id just a new "predicate name".

This can be very useful to present the same reality in another perspective/point of view.

## Filters
 
If we have: `s p o ; q a .`

We can define a subgraph by "removing" the  `q`  predicate:

```
graph(s , 1) \ {q} => s p o .
```

## Classical inferences

The use of classical inferences is very important also.

## Temporal inferences

If we have:

```
s p(t1) a .
s p(t2) b .
p(t1) a P .
p(t2) a P .
P a Time_Predicate .
```

and a and b were not existing before the predicates were created, we could deduce:

```
a before b .
```

Not sure it is useful.

Simpler like that:

```
a2 previous a1 .
a3 previous a2 .
=> a3 previous a1 .
```

Some predicates can have special transitivity features.

## Special predicates

  * Transitive predicates
  * 


Ou a2 previous a1 . et a3 previous a2 . => a3 previous a1 .
On pourrait tagguer les relations associatives :
previous type associative .
imply type associative .
In pourrait tagguer les relations commutatives
synonyme type commutative .

Revoir la notion de liste

L’inversion des triples q = inverse(p)
s p o . implique o q s .
Et on peut avoir une chaîne sémantique avec des inverses.


Action : regarder le temporel de gruf

Il y a 2 sujets :
La création du graph sémantique depuis la grammaire
Les transfos de graphe


En chantier :
Premier sujet :
Pour un sujet s : trouver tous les x p : 
s p? x? et x? p? s

