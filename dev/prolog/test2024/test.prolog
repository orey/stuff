myreplace([A|L],[first|L]).

pred1([A|L], L).

inc([],[]).
inc([A|L],[A1|L1]) :- A1 is A+1, inc(L,L1).

putfirst(A,M,[A|M]).

writeall([]).
writeall([A|[]]) :- write(A).
writeall([A|L]) :- write(A),write(','),writeall(L).

putlast(A,M,L) :- append(M,[A],L).

