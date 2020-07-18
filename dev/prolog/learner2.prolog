% learns capitals

my_assertz(Z) :- open('capitals.prolog', append, Handle),
                 write(Handle, Z),
                 write(Handle, ".\n"),
                 close(Handle).

my_capital(X) :- capital(X,Y),
		 write("Capital of "), write(X), write(" is: "), write(Y), nl.

my_capital(X) :- not(capital(X,Y)), not(X = stop), write("I don't know the answer. Please tell me: "),
                 read(Y), my_assertz(capital(X,Y)), write("Thanks!"), nl.

%loop :- repeat,
%	consult("capitals.prolog"), write("Country? "), read(X), my_capital(X),
%	X = stop,
%	!.

end_condition(stop) :- write("Goodbye.").


play :- write("CAPITAL GAME: write country name and I will tell you the capital."),nl,
        write("Write STOP to stop playing. And don't forget the . at the end."),nl,
	repeat,
	consult("capitals.prolog"), write("Country? "), read(X),
	my_capital(X),
	end_condition(X).

