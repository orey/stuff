statement(a,friend(b)).
statement(a,enemy(c)).
statement(b,not(in(b))).
statement(b,not(friend(b))).
statement(b,not(enemy(b))).
statement(c,in(c)).
statement(c,in(a)).
statement(c,in(b)).

% spot friend inconsistencies
disagree_friend(X, Z, Y) :- statement(X,friend(Y)), statement(Z, not(friend(Y))),
                            write(X), write(" and "), write(Z),
                            write(" disagree on the fact that "), write(Y),
                            write(" was a friend of the victim"), nl, fail.

disagree_friend2(X, Z, Y) :- statement(X,friend(Y)), statement(Z, not(friend(Y))).

% spot places inconcistencies
disagree_place(X, Y, Z) :- statement(X, in(Z)), statement(Y, not(in(Z))),
                            write(X), write(" and "), write(Y),
                            write(" disagree on the fact that "), write(Z),
                            write(" was out"), nl, fail.

disagree_place2(X, Y, Z) :- statement(X, in(Z)), statement(Y, not(in(Z))).


disagree1(X,Y1,Y2,Z1,Z2) :- disagree_friend2(X,Y1,Z1),disagree_place2(X,Y2,Z2).
disagree2(X1,X2,Y,Z1,Z2) :- disagree_friend2(X1,Y,Z1),disagree_place2(X2,Y,Z2).

disagree2bis(X1,X2,Y,Z1,Z2) :- disagree_friend2(X1,Y,Z1),disagree_place2(X2,Y,Z2),
                               write(X1), write(" and "), write(X2),
                               write(" agree on the fact that "), write(Y),
                               write(" disagrees with them both, "),
                               write("respectively on friend and place. "),
                               write(Y), write(" is the guilty one."), nl, fail.

