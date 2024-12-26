#!/bin/bash

if [ $# != 2 ]
then
    echo "run-function.sh: Script version 1"
    echo "Runs function in a js file with nodejs"
    echo "Usage : run-function.sh [file.js] [function]"
    echo "[function] must have no parameters"
    exit 0
fi

jsfile=$1
jsfunction=$2

echo "Calling $2 in $1"
node | echo "-e 'require(\"./$1\").$2()'"
node --version
ode -e "'require(\"./$1\").$2()'"

echo "Done"

