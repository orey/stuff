'use strict';

//--------------------------------------------
// Constructor defined in the JS the Good parts
//--------------------------------------------

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
//other_person.age  = 46;

console.log(Person);
console.log(Object.getPrototypeOf(Person));
console.log('---------------------')

console.log(other_person);
console.log(Object.getPrototypeOf(other_person));
console.log(other_person.age);
console.log('---------------------')


//--------------------------------------------
// Function version of the Object.create
//--------------------------------------------

const ChainFactory = function (o) {
    var F = function () {};
    F.prototype = o;
    return new F();
};

var per = ChainFactory(Person);
per.age = 25;

console.log(per);
console.log(Object.getPrototypeOf(per));
console.log(per.name);
console.log('---------------------')

//--------------------------------------------
// Construct function with a private variable
//--------------------------------------------

const construct = function(proto){
    var that, priv = 'Private variable';
    proto = proto || {};
    that = ChainFactory(proto);
    that.pub = "Public variable";
    that.getPriv = function(){return priv};
    that.setPriv = function(temp){priv = temp;}
    return that;
}

var aaa = construct(Person);
console.log(aaa);
console.log(aaa.name);
console.log(aaa.pub);
aaa.pub = 'aaa';
console.log(aaa.pub);
console.log(aaa.getPriv());
aaa.setPriv('aaa');
console.log(aaa.getPriv());
console.log(aaa);
console.log('---------------------')

var bbb = construct(Person);
console.log(bbb);
console.log(bbb.name);
console.log(bbb.pub);
bbb.pub = 'bbb';
console.log(bbb.pub);
console.log(bbb.getPriv());
bbb.setPriv('bbb');
console.log(bbb.getPriv());
console.log(bbb);
console.log('---------------------')

var y = {a: 12, b: "string"};
y.prototype = Object;
var z = y.create();
z.c = 45
console.log(z);








