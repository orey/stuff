import os
from spire.presentation.common import *
from spire.presentation import *

INPUT = "C:\\ProgramData\\orey\\data\\outlook\\test2\\"
OUTPUT = "C:\\ProgramData\\orey\\data\\outlook\\test2\\output\\"

def breakpoint():
    answer = input("Breakpoint. Continue? [y/Y] ")
    if not answer.upper() == "Y":
        print("Goodbye...")
        exit()


for subdir, dirs, files in os.walk(INPUT):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".pptx"):
            print (filepath)
            # Create a Presentation instance
            ppt = Presentation()

            # Load a PowerPoint document
            ppt.LoadFromFile(filepath)

            #Save the document to HTML format
            ppt.SaveToFile(os.path.join(OUTPUT, file[:-5] + ".html"), FileFormat.Html)
            ppt.Dispose()
            breakpoint()
            continue
        else:
            continue

    


