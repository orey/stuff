import pandas as pd
import os
 
# Get the list of all files and directories
path = "."
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)

for f in dir_list:
    if f.endswith(".xlsx"):
        print("Treating " + f)
        data_xls = pd.read_excel(f, 'Report Data 1', index_col=None)
        data_xls.to_csv(f+".csv")
