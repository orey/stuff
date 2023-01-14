# Tips for configuring sbcl under Linux

## Recalling last command from the comand line

sbcl does not recall last command when interactive CLI. A way to do it is to install the `rlwrap` linux package.

```
$ su root
# apt install rlwrap
# exit
```

Then rlwrap the sbcl command to get the feature.

```
$ rlwrap sbcl
```



