# Comparison of scripting language constructs

## Introduction

Going from a language to another is quite painful. This page gathers some correspondance between languages.

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




    
