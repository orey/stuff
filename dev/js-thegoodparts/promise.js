"use strict";

let toto = 12;

let p = new Promise((resolve, reject) => {
    if (toto == 13){
        console.log("resolved");
        resolve(toto);
    }
    else
    {
        console.log("rejected");
        reject("bad stuff");
    }
});

p.then(param => console.log("Dans le then: " + param))
    .catch(truc => console.log("Dans le catch: " + truc));





