% 
mange(chevre,chou).
mange(loup,chevre).

depart(loup).
depart(chevre).
depart(chou).

arrivee(loup) :- depart(X), mange(X, Y).




