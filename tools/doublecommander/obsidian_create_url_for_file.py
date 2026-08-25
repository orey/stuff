import sys, pyperclip
from urllib.parse import quote

#print(sys.argv)
# 1. get paramater from command line
origin = sys.argv[1].replace("\\","/")
filename = origin.split("/")[-1]
stringtoformat = f"[{filename}]({'file:///' +  quote(origin)})"
pyperclip.copy(stringtoformat)

print("Link for obsidian created and copied in the clipboard")
print(stringtoformat)
