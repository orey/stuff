import sys,os

sys.path.append('.')
from tools import footprint_sha1, interrupt, list_files_in_dir, CounterDict, print_dict


WIN = "C:\\ProgramData\\orey\\data\\outlook\\202502-txt"
LINUX = "/home/olivier/olivier-data/202502/"


TOKENS = [
    "From:",
    "Sent:",
    "To:",
    "Cc:",
    "Subject:",
    "Attachments:"
]

class Mail():
    def __init__(self, mailtext):
        tab = mailtext.split("\n")
        for line in tab:
            interrupt(line)
            for token in TOKENS:
                if line.startswith(token):
                    print(token + " - " + line.replace(token, "").strip())
                    



def analyze_mail(mail):
    with open(mail, 'r', encoding="latin_1") as doc:
        content = doc.read()
        interrupt(content)
        mail = Mail(content)



def main():
    arr = list_files_in_dir(LINUX)
    print(arr)
    dic = CounterDict()
    exts = CounterDict()
    for f in arr:
        #-1 calculate footprints
        dic.append(footprint_sha1(LINUX + f))
        #-2 get extensions
        temp = f.split(".")
        if len(temp) == 1:
            # no extension
            exts.append("no extension")
        else:
            exts.append(temp[-1])
            if temp[-1] == "txt":
                analyze_mail(LINUX + f)
            
    print_dict(exts.dic)

    d = dic.dic
    for key, value in d.items():
        if value != 1:
            print(key + " | " + str(value))



if __name__ == "__main__":
    main()
                
