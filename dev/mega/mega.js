"use strict";
const dice = require('./dice.js');

const ECHEC_CRITIQUE = -1;
const REUSSITE_CRITIQUE = 1;
const NORMAL = 0;

class Perso {
    constructor(name, comp,pdv,cha,psy) {
        this.name = name;
        this.comp = comp;
        this.pdv = pdv;
        this.cha = cha;
        this.psy = psy;
    }

    combat(){
        let roll = dice.roll("2D6");
        if (roll == 2) {
            return [ECHEC_CRITIQUE, roll + this.comp];
        }
        if (roll == 12) {
            return [REUSSITE_CRITIQUE, roll + this.comp];
        }
        return [NORMAL, roll + this.comp] ;
    }
    
}

function process_critique(data) {
    if (data == ECHEC_CRITIQUE) 
        return "Echec critique";
    if (data == REUSSITE_CRITIQUE) 
        return "Réussite critique";
    return "";
}

function combat(p1, p2) {
    let c1 = p1.combat();
    let c2 = p2.combat();
    console.log(p1.name + " : " + String(c1[1])
                + " - " + p2.name + " : " + String(c2[1]));
    if (c1[1] > c2[1]) {
        console.log("Le vainqueur est : " + p1.name + ".");
        console.log(process_critique(c1[0]));
    }
    else {
        if (c1[1] < c2[1]) {
            console.log("Le vainqueur est : " + p2.name + ".");
            console.log(process_critique(c2[0]));
        }
        else{
            console.log("Les deux joueurs sont ex-aequo.");
        }
    }
}

let perso1 = new Perso("Gary Gygax",
                       dice.roll("1D3+3"), 
                       dice.roll("2D6+6"), 
                       dice.roll("1D6+6"),
                       dice.roll("1D3+3"));

let perso2 = new Perso("Dave Arneson",
                       dice.roll("1D3+3"), 
                       dice.roll("2D6+6"), 
                       dice.roll("1D6+6"),
                       dice.roll("1D3+3"));

console.log(perso1);
console.log(perso2);

combat(perso1, perso2);




