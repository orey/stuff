"use strict";

let toto = 12;

let p = new Promise((resolve, reject) => {
    if (toto == 12){
        console.log("resolved");
        resolve(toto);
    }
    else
    {
        console.log("rejected");
        reject("bad stuff");
    }
});

p.then(param => {
    console.log("Dans le then: " + param);
    return {a : 1, b : 2};
})
    .catch(truc => {
        console.log("Dans le catch: " + truc);
        throw new Error("pour le suivant");
    })
    .then(obj => {
        console.log("Au deuxième niveau");
        console.log(JSON.stringify(obj));
    })
    .catch(err => console.log("Second niveau: " + err));
          





