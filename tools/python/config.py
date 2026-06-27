'''
This class is here to read and create a config file
The objective is that most programs will run as follows:
> python theprogram.py config.ini
If the config.ini is not present, the program will search for a config.ini
that has the name of the program. Here theprogram.ini
'''

import configparser, sys, os

DEFAULT_VALUE = "NOT SET"


#--------------------------------ensure files
def ensureFile(f):
    return True if os.path.isfile(f) else False

    
#----------------------------------------------- Config
class Config:
    '''
    Simple section/key-value config
    params = {
        "section1" : ["key1", "key2", "key3", etc.],
        "section2" : ["key4", "key5", "key6", etc.],
        etc
    }
    '''
    def __init__(self, params={}, configfilename=""):
        '''
        params is the array of parameters to get
        This parameter is mandatory (list of strings
        '''
        self.conf = configparser.ConfigParser()
        if params == {}:
            raise Exception("Error in Config: need params")
        self.params = params
        if configfilename == "":
            temp = sys.argv[0]
            # Building the default config name
            self.conffilename = temp.replace(temp.split(".")[-1],"") + "ini"
        else:
            self.conffilename = configfilename
        print(f"Info: Config name: {self.conffilename}")
        if not ensureFile(self.conffilename):
            self.create_config()
            print("Warning: As no config file was found, the program created a default one: "
                  + f"{self.conffilename}\nPlease fill in the parameters")
            return
        # read the config file following the params and warn the user
        self.conf.read(self.conffilename)
        allsectionskey = True
        for section in self.params:
            for key in self.params[section]:
                if not self.conf.has_option(section, key):
                    print(f"Warning: Section {section} and key {key} not in the config file")
                    allsectionskey = False
        if allsectionskey:
            print(f"Info: Configuration file '{self.conffilename}' OK. All sectons and key set.")

    #-------------------------- create_config
    def create_config(self):
        for section in self.params:
            self.conf[section] = {}
            for key in self.params[section]:
                self.conf[section][key] = DEFAULT_VALUE
        with open(self.conffilename, 'w') as f:
            self.conf.write(f)

    #-------------------------- get_value
    def get_value(self, section, key):
        return self.conf[section][key]

    
#============================================================ main
if __name__ == "__main__":
    params = {
        "section1":["key1","key2"],
        "section2":["key3","key4"]
    }
    try:
        voidconfig = Config(params)
    except Exception as e:
        print(f"Exception {e}")
    except Warning as w:
        print(f"Warning {w}")
    try:
        config = Config(params, "toto.ini")
    except Exception as e:
        print(f"Exception {e}")
    except Warning as w:
        print(f"Warning {w}")
    try:
        config = Config(params, "test.ini")
    except Exception as e:
        print(f"Exception {e}")
    except Warning as w:
        print(f"Warning {w}")
    
    
                        
