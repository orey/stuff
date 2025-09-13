from pypdf import PdfReader

import json, os, os.path, csv
import sys
sys.path.append('.')
from tools import interrupt, generateName, ensureFolder, ensureFile

#ENCODING = "utf8"
ENCODING = "latin_1"


#==================================================================== Dain
class Dain():
    def __init__(self, filename):
        self.filename = filename
        self.dict = {}
    def add(self, key, value):
        self.dict[key] = value
    def __str__(self):
        st = "Dain file: " + self.filename
        for key in self.dict:
            st += "\n- " + key + ": " + self.dict[key]
        return st
        

#==================================================================== extract_text_from_pdf
def extract_text_from_pdf(myfile, encode=ENCODING, dumpfiletext = False):
    try:
        # creating a pdf reader object
        reader = PdfReader(myfile)

        # printing number of pages in pdf file
        l = len(reader.pages)
        #print(f"Found {l} pages in {os.path.basename(myfile)}, encoding: {encode}")

        # getting the texts
        mytext = ""
        for i in range(l):
            mytext += reader.pages[i].extract_text()
        if dumpfiletext:
            try:
                with open(myfile+".txt", 'w', encoding=encode, newline='') as output:
                    output.write(mytext)
                print(myfile+".txt created")
            except Exception as e:
                print(f"A problem occured on dumping the text of file '{myfile}'")
                print(e)
                print(mytext)
                #input("Press return to continue ")
        return mytext
    except Exception as e:
        print(f"An error was detected while reading the PDF: {myfile}")
        print(f"Skipping...")
        return ""


#========================================== clean_rough_text
def clean_rough_text(rough, action, params=""):
    rough_text = rough.strip()
    if action == "DATA":
        return rough_text
    elif action == "SPLIT_FIRST":
        return rough_text.split(params)[0].strip()
    elif action == "SPLIT_SECOND":
        temp = rough_text.split(params)
        return rough_text.replace(temp[0], "").strip()
    elif action == "SPLIT_LAST":
        return rough_text.split(params)[-1].strip()
    elif action == "FIRST_X":
        return rough_text[int(params):]
    elif action == "REMOVE_FIRST_LAST":
        temp = rough_text.split(params)
        #interrupt(temp)
        return rough_text.replace(temp[0], "").replace(temp[-1], "").strip()
    else:
        print(f"Action: '{action}' not known.")
        return ""
              
    

#========================================== fill_dain_object
def fill_dain_object(dain, conf, thetex, verbose = False):
    tex = thetex.replace("\n"," ").replace("\t"," ")
    for key in conf:
        value = conf[key]
        if key == "name" and verbose:
            print(f"Config: '{value}'")
            continue
        if key == "start" and verbose:
            print(f"Start string: '{value}'")
            continue
        if type(value) is list:
            # --------------------------------------MIDDLE
            if value[0] == "MIDDLE":
                # we are not at the end
                # we can expect 1: begin chain, 2: end chain,
                # 3: action, 4: params (optionnal)
                try:
                    begin = tex.index(value[1])
                except ValueError:
                    if verbose:
                        print(f"Warning: The start chain '{value[1]}' was not found.")
                    dain.add(key, "")
                    continue
                try:
                    end = tex.index(value[2])
                except ValueError:
                    if verbose:
                        print(f"Warning: The end chain '{value[2]}' was not found.")
                    dain.add(key, "")
                    continue
                rough_text = (tex[begin + len(value[1]):end]).strip()
                # manage rough text
                if len(value) == 4:
                    # no params
                    data = clean_rough_text(rough_text, value[3])
                else:
                    data = clean_rough_text(rough_text, value[3], value[4])
                dain.add(key, data)
                #if verbose:
                #    print(f"{key} : {data}")
                #    interrupt()
                continue
            # --------------------------------------AFTER
            elif value[0] == "AFTER":
                # we are not at the end
                # we can expect 1: begin chain, 2: length to get
                try:
                    begin = tex.index(value[1])
                except ValueError:
                    if verbose:
                        print(f"Warning: The start chain '{value[1]}' was not found.")
                    dain.add(key, "")
                    continue
                startindex = begin + len(value[1])
                dain.add(key, tex[startindex : startindex + int(value[2])])
            # --------------------------------------BEFORE
            elif value[0] == "BEFORE":
                # 1: end chain, 2: action, 3: params
                lines = thetex.split('\n')
                indexl = 0
                for line in lines:
                    if line.strip().startswith(value[1]):
                        break;
                    else:
                        indexl += 1
                rough_text = lines[indexl - 1]
                if len(value) == 4:
                    data = clean_rough_text(rough_text, value[2], value[3])
                    dain.add(key, data)
            # --------------------------------------UNKNOWN<
            else:
                print(f"Unknown grammar element: '{value[0]}'")


#========================================== usage
def usage():
    print(
'''
|--------------------------------------------------------------------------------------|
| Tool to extract data from DAINs. This tool takes 1 parameter, the folder to analyze. |
| It manages 2 kinds of DAINs (1 page DAIN and 3 pages DAIN). If you have other types  |
| if DAINs to manage, please contact the NHI IT department.                            |
| Usage:                                                                               |
| C:\\a_folder\\another_folder> get_data_from_pdf_dain.exe "R:\\folder1\\folder2"          |
|--------------------------------------------------------------------------------------|''')
    sys.exit()

#========================================== read_config
def read_config(verbose = False):
    try:
        with open('config.json', encoding='utf8') as f:
            config = json.load(f)
            if verbose:
                print(config)
            return config
    except FileNotFoundError:
        print("Configuration file 'config.json' was not found. Please provide it.")


#========================================== Main
def main():
    #print(sys.argv)
    if len(sys.argv) == 1:
        usage()
    if len(sys.argv) != 2:
        print("Warning: only the first parameter is taken into account")
    #--- 1. Ensure folder exists
    folder = sys.argv[1]
    if folder.endswith('"'):
        # known problem of the folder "C:\test test\" finishing by a \
        # The " char is added to the folder and the folder is not recognized
        folder = folder[:-1]
    exists = ensureFolder(folder)
    if not exists:
        print(f"Folder '{folder}' does not exist. Exiting...")
        sys.exit()
    #--- 2. Read the configuration file to get encoding and debug mode
    config = read_config(False)
    encode = config["encoding"]
    debugmode = True if config["debugmode"] == "True" else False
    if debugmode:
        print("Debug mode on")
    else:
        print("Debug mode off")
    #--- 3. Create dain array and instantiate log file
    dains = []
    logs = "Hereafter is the list of files that were not processed because no grammar was found to extract data.\n---\n"
    files_ok = 0
    files_not_ok = 0
    #--- 4. Explore list of files
    for f in os.listdir(folder):
        completefilename = os.path.join(folder, f)
        extension = f.split('.')[-1]
        if ensureFile(completefilename) and extension in ['pdf','PDF']:
            print(f"Processing file {f}")
            #g = analyze_file(completefilename, False)
            tex = extract_text_from_pdf(completefilename, encode, debugmode)
            theconf = None
            for conf in config["configs"]:
                if tex.startswith(conf["start"]):
                    theconf = conf
            if theconf == None:
                print(f"=> Warning: The file {f} has no matching configuration.")
                logs += f + "\n"
                files_not_ok += 1
                continue
            dain = Dain(completefilename)
            fill_dain_object(dain, theconf, tex, debugmode)
            if debugmode:
                print(dain)
            #interrupt()
            dains.append(dain)
            files_ok += 1
            print("=> OK")
    #--- 5. Write log file
    logfilename = generateName("_files_not_treated.txt")
    with open(logfilename, "w", encoding=ENCODING) as log:
        log.write(logs)
    #--- 6. Write CSV file from dain objects
    csvfilename = generateName("_dains.csv")
    with open(csvfilename, 'w', encoding=ENCODING, newline='') as output:
        writer = csv.writer(output, delimiter = ';')
        #create header
        header = list(dains[0].dict.keys())
        writer.writerow(["file_name"] + header)
        for d in dains:
            writer.writerow([d.filename] + list(d.dict.values()))
    #--- 7. End
    print("End of treatment")
    print(f"Files treated and added to the csv file: {files_ok}")
    print(f"Files not added to the csv file: {files_not_ok}")
    print(f"For more details, consult the log file: {logfilename}")
        

#============================================== entry point
if __name__ == '__main__':
    main()

                
