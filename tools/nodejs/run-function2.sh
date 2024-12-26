#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <javascript_file> <function_name>"
    exit 1
fi

# Assign the arguments to variables
javascript_file=$1
function_name=$2

# Check if the JavaScript file exists
if [ ! -f "$javascript_file" ]; then
    echo "Error: File '$javascript_file' not found."
    exit 1
fi

# Execute the function in the JavaScript file using Node.js
node -e "
const fs = require('fs');
const path = require('path');
const filePath = path.resolve('$javascript_file');
const code = fs.readFileSync(filePath, 'utf8');
eval(code);
if (typeof $function_name === 'function') {
    $function_name();
} else {
    console.error(\"Error: Function '$function_name' not found in the file.\");
    process.exit(1);
}"


