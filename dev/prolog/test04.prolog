room(kitchen).
room(office).
room(hall).
room('dining room').
room(cellar).

location(desk, office).
location(apple, kitchen).
location(flashlight, desk).
location('washing machine', cellar).
location(nani, 'washing machine').
location(broccoli, kitchen).
location(crackers, kitchen).
location(computer, office).

what_is_in(X) :-
    location(Y,X),
    write(Y),nl,
    fail.

door(office, hall).
door(kitchen, office).
door(hall, 'dining room').
door(kitchen, cellar).
door('dining room', kitchen).

edible(apple).
edible(crackers).

tastes_yucky(broccoli).

eatable_in(X) :-
    (edible(Y);tastes_yucky(Y)),
    location(Y,X),
    write("Eatable: "),
    write(Y),
    write(" in "),
    write(X),nl,
    fail.

turned_off(flashlight).

here(kitchen).

