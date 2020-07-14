% learns capitals

test(X) :- (X = "STOP."), write("Goodbye!"), nl.

loop_step :- consult("capitals.prolog"), write("Country? "), read(X),
             not(test(X)), my_capital(X),
             loop_step, fail.

my_assertz(Z) :- open('capitals.prolog', append, Handle),
                 write(Handle, Z),
                 write(Handle, ".\n"),
                 close(Handle).

my_capital(X) :- not( X = stop), capital(X,Y), write("Capital of "), write(X), write(" is: "), write(Y), nl.
my_capital(X) :- not( X = stop), write("I don't know the answer. Please tell me: "),
                 read(Y), my_assertz(capital(X,Y)), write("Thanks!"), nl.

play :- write("CAPITAL GAME: write country name and I will tell you the capital."),nl,
        write("Write STOP to stop playing. And don't forget the . at the end."),nl,
        loop_step.


