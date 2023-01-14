# Comparison of scripting language constructs

## Introduction

Going from a language to another is quite painful. This page gathers some correspondance between languages.

## Load a file in REPL and exiting REPL

Js

```
$ node
> .load my_file.js
>
> .exit
```

## Tokenizing a string

Js

```
let str = "This is a test";
// splits at the spaces and returns an array
let res = str.split(" ");
```

## String to int

Js

```
let myvar = parseInt("10");
```

## String to int

Js

```
let num = 15;
let myvar = num.toString();
```

## Add element to list

Js array

```
let myvar = [12, 15, 20];
myvar.push(56);
```


## Objects

JS

```
class MyClass {
    constructor(param1, param2) {
        this.member = 12;
        blah();
    }
    
    set member(x) {
        this.member = x;
    }
    
    get member() {
        return this.member;
    }

}
```

None existing objects are ```undefined```.


## True and False

JS

```
let a = true;
let b = false;
```



## Functions and procedures

Python

```
def myFunction (param1, param2):
    blah(param1)
    return 12
```

VBA Procedure - no return value

```
Sub MyProcedure(param1 As String, param2 As Integer)
    blah(param1)
    Return
End Sub
```

VBA Function - return value

```
Function MyFunction(param1 As String, param2 As Integer)
    blah(param1)
    MyFunction = param2 + 2
End Function
```

JS

```
function MyFunction(param1, param 2) {
    blah(param1);
    return 12;
}

let MyFunction = (param1, param 2) => {
    blah(param1);
    return 12;
}
```

## While loop

VBA

```
Do While myTest = 0
   DoSomething()
Loop
```


## Concat strings

VBA

```
ConcatString = string1 & string 2
```




    
