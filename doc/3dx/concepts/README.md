# 3DX

This repo proposes a view of all modules in 3DX.

## Warning

Airbus Group has a contract with DS and all modules available in 3DX could not be accessible by Airbus within the terms of the contract.

## Data source

As of April 24 2019, the list of all trigrams is [here](https://www.3ds.com/terms/product-portfolio/licensed-programs/).

The URL to get all licenced programs is [here](https://www.3ds.com/no_cache/terms/product-portfolio/licensed-programs/?ajax_get_products=1).

## Notes

  * The original file comes with parenthesis at the beginning and at the end of the file. Those parenthesis must be removed in order for python to parse the file properly.
  * Converter note: in order to see more fields, you have the extend the values in `FIELD_NAMES`

## Content of the folder

  * Input data files
    * `20190424.json`: original file
    * `20190424-bis.json`: original file without the parenthesis
  * Program
    * `setenv.bat`: sets the Python 3.7 environment under Windows
    * `convert.py`: The python converter
  * Output data files
    * `modules.csv`: CSV file with modules
    * `20190424_3DX-modules.xlsx`: Excel file corresponding to the public offer in terms of modules
    
