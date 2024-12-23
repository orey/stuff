% learns capitals

my_assertz(Z) :- open('capitals.prolog', append, Handle),
                 write(Handle, Z),
                 write(Handle, ".\n"),
                 close(Handle).

% Original implementation with a repetition of the test condition in
% my_capital second clause. Indeed, a cut in the first clause is simpler.
% When the choice is exclusive, it is better to cut.
% If there is an exception to a list, we can cut with failure.
%
/*my_capital(X) :- capital(X,Y),
		 write("Capital of "), write(X), write(" is: "), write(Y), nl.
my_capital(X) :- not(capital(X,Y)),
		 write("I don't know the answer. Please tell me: "),
                 read(Y), my_assertz(capital(X,Y)), write("Thanks!"), nl.*/

my_capital(X) :- capital(X,Y),
		 write("Capital of "), write(X), write(" is: "), write(Y), nl, !.
my_capital(X) :- write("I don't know the answer. Please tell me: "),
                 read(Y), my_assertz(capital(X,Y)), write("Thanks!"), nl.

loop :- consult("capitals.prolog"), write("Country? "), read(X),
	X \= stop, my_capital(X), loop.

end_condition(stop) :- write("Goodbye.").

play :- write("CAPITAL GAME: write country name and I will tell you the capital."),nl,
        write("Write STOP to stop playing. And don't forget the . at the end."),nl,
	loop.


