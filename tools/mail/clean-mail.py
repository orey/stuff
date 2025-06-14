import os

def listFilesInDir(rootdir):
    '''
    Warning rootdir does not 
    '''
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            #print(os.path.join(subdir, file))
            filepath = subdir + os.sep + file

            if filepath.endswith(".txt"):
                print(filepath)



def main():
    listFilesInDir("C:\\ProgramData\\orey\\data\\outlook\\202502-txt")
                
if __name__ == "__main__":
    main()
                
