if (typeof Object.create !== 'function') {
    Object.create = function (o) {
	var F = function () {};
	F.prototype = o;
	return new F();
    };
}

var Person = {name:"Morgane",age: 6};
var other_person = Object.create(Person);
other_person.name = "Nathalie";
other_person.age  = 46;




