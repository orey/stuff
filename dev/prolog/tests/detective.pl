are_friends(X,Y) :- friend(Y,X) ; friend(Y,X).
are_friends(X,Y) :- not(enemy(X,Y)) ; not(enemy(Y,X)).

are_enemies(X,Y) :- enemy(X, Y) ; enemy(Y,X).
are_enemies(X,Y) :- not(friend(X,Y)) ; not(friend(Y,X)).

not_knowing(X,Y) :- not(are_enemies(X,Y)), not(are_friends(X,Y)).

crime_time(X,in) :- not(crime_time(X,out)).
crime_time(X,out) :- not(crime_time(X,in)).

statement(a,friend(v,b)).
statement(a,enemy(c,v)).

statement(b,crime_time(b,out)).
statement(b,not_knowing(b,v)).

statement(c,crime_time(c,in)).
statement(c,crime_time(a,in)).
statement(c,crime_time(b,in)).

