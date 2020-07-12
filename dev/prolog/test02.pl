
mange(chevre,chou) :- lieu(chevre, chou, _).
mange(loup,chevre).

depart(loup).
depart(chevre).
depart(chou).

arrivee(X) :- depart(X), not(mange(Y, Z)), not(mange(Z, Y)) .
depart(Y)  :- arrivee(Y) not(mange(X, Z)), not(mange(Z, X)) .

arrivee(loup)   :- depart(loup), not(mange(chevre, chou)).
arrivee(chevre) :- depart(chevre).
arrivee(chou)   :- depart(chou), not(mange(loup, chevre)).

