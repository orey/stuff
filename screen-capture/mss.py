from mss import mss
from datetime import datetime
import os, sys

from pathlib import Path

TARGET = 'C:/Users/Toto/_Screens'

if __name__ == "__main__":
    folder = input ("== Screen capture ==\nProvide a folder: ")
    if folder == "":
        folder = "default"
    targetdir = os.path.join(TARGET, folder)
    if not os.path.isdir(targetdir):
        os.makedirs(targetdir)
    image = ""
    shotnumber = 0
    while True:
        q = input("Shot? [y/n] ")
        if q != "y":
            print("=> " + str(shotnumber) + " screenshots recorded in " + targetdir)
            print("Bye")
            s = input("Type any key to exit")
            exit(1)
        with mss() as sct:
            image = sct.shot()
            shotnumber += 1
            print("Shot done")
        if image == "":
            print("Capture failed. Exiting.")
            exit(0)
        os.rename (os.path.join(os.getcwd(),image), \
                   os.path.join(targetdir, datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".png"))
        
