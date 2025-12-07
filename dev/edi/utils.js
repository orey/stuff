/*******************************************************
Utils
Author: rey.olivier@gmail.com
Date: November 2025
License: GNU GPL v3
******************************************************/
"use strict";

//================================================= Fine grain management of chars
const ALPHA = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
               "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
const EXTENDED_ALPHA = ALPHA.concat([" ","-"]);
const NUMERIC = ["0","1","2","3","4","5","6","7","8","9"];
const EXTENDED_NUMERIC = NUMERIC.concat([".",","]);
const ALPHANUMERIC = ALPHA.concat(NUMERIC);
const EXTENTED_ALPHANUMERIC = EXTENDED_ALPHA.concat(EXTENDED_NUMERIC);


//================================================= isAlphaNumeric
//TODO: after testing see if we can use EXTENDED_ALPHANUMERIC especially for the space
function isAlphaNumeric(str) {
    // pure alpha numeric does not contain spaces
    if (str.match(/^[a-z0-9]+$/i) == null) {
        console.warn("The string is not fully alphanumeric. The following characters are theoretically illegal:");
        let acc = []
        for (let c of str)
            if (! ALPHANUMERIC.includes(c))
                if (!acc.includes(c))
                    acc.push(c);
        console.warn(acc);
        return true;
    }
    else
        return true;
    //Alpha numeric including space
    //return str.match(/^[\w\-\s]+$/) != null
}


//================================================= isAlpha
//TODO: after testing see if we can use EXTENDED_ALPHA
function isAlpha(str) {
    if (str.match(/^[a-z]+$/i) == null){
        console.warn("The string is not fully alpha. The following characters are theoretically illegal:");
        let acc = []
        for (let c of str)
            if (! ALPHA.includes(c))
                if (!acc.includes(c))
                    acc.push(c);
        console.warn(acc);
        return true;
    }
    else
        return true;
}


//================================================= isNumeric
//TODO: after testing see if we can use EXTENDED_NUMERIC
function isNumeric(str) {
    if (str.match(/^[0-9]+$/i) == null) {
        console.warn("The string is not fully numeric. The following characters are theoretically illegal:");
        let acc = []
        for (let c of str)
            if (! NUMERIC.includes(c))
                if (!acc.includes(c))
                    acc.push(c);
        console.warn(acc);
        let rc = true;
        for (let c of acc)
            if (! c in EXTENTED_ALPHANUMERIC) {
                console.warn("'" + c + "' is not an extended character");
                rc = false;
            }
        return rc;
    }
    else
        return true;
}

//================================================== teststrings
function testStrings(){
    let testcases = [
        "123456",
        "AzertuiopZZ",
        "12azerY",
        "_gsf-'",
        "kgshfs%$£",
        "Le vierge le vivace et le bel aujourd'hui",
        "Va-t-il nous dechirer d'un coup de son aile ivre"
    ];
    for (let test of testcases) {
        console.log("-------------------------")
        console.log("--- Test case for '" + test + "'");
        console.log("- isAlphaNumeric? " + isAlphaNumeric(test));
        console.log("- isNumeric? " + isNumeric(test));
        console.log("- isAlpha? " + isAlpha(test));
    }
}

testStrings()

//================================================== Exports
module.exports = {
    isAlphaNumeric,
    isAlpha,
    isNumeric
};


