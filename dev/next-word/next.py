from unidecode import unidecode
import sys

ADD_SPACE_AROUND = [".",",",";",":","!","?","'",'"',"-","(",")","—"]
REPLACE = [
    ("\n", " "),
    ("_" , " "),
    ("”" , '"'),
    ("‘" , "'"),
    ("“" , '"')
]

PADDING_SIZE = 4

#----------------------------------------------------------------------breakpoint
def breakpoint(obj=None):
    if obj: print(obj)
    a = input("Do you want to continue? ('n' will stop) ")
    if a == "n":
        print("Goodbye")
        sys.exit()
    

#-----------------------------------------------------------------------manual_tokenizer
def manual_tokenizer(f, verbose = False):
    '''
    More basic stuff but working quite well
    '''
    with open(f) as g:
        text = g.read()[1:] #removing first char \ufeff
        if verbose: print("Text read")
        text = unidecode(text)
        if verbose: print("Accents removed")
        text = text.lower()
        if verbose: print("Text in lower case")
        for before, after in REPLACE:
            text = text.replace(before, after)
            if verbose: print(f"{before} was replaced by {after}")
        for char in ADD_SPACE_AROUND:
            text = text.replace(char," " + char + " ")
            if verbose: print("Created spaces around << " + char + " >>")
        return [x for x in text.split(" ") if x] #removing empty strings


#-----------------------------------------------------------------------build_dict    
class WordDict:
    '''
    The dict maintains a dictionary that is the images of all the provided text
    Sequentially, all words are assigned a token. The number of occurrences
    of words is counted.
    The dict enables to parse text and get back an array of tokens.
    '''
    def __init__(self):
        '''
        creates a dict with
        dict key : word
        dict value : [
               string padded of integer_representation (auto-increment counter),
               nb_occurences of the word in the texts that were provided
            ]
        '''
        self.dic = {}
        self.count = 0
        
    def add_words(self, words, verbose= False):
        '''
        words : array of words
        returns the array of tokens
        '''
        tokenized_words = []
        for word in words:
            if word in self.dic:
                # adding a new occurence
                rep = self.dic[word][0]
                tokenized_words.append(rep)
                occ = self.dic[word][1]
                self.dic[word] = [rep, occ+1]
            else:
                # adding the word in dic
                rep = ("{:0"+ str(PADDING_SIZE)+"d}").format(self.count+1)
                tokenized_words.append(rep)
                self.dic[word] = [rep, 1]
                self.count +=1
        if verbose:
            print(self)
        return tokenized_words

    def __str__(self):
        st = ""
        temp = dict(sorted(self.dic.items()))
        for elem in temp:
            st += f"{elem} ({temp[elem][1]}) | "
        st += f"\nDictionary length is {len(self.dic)}\n"
        return st

    def decode(self, st):
        st_elems = []
        for i in range(int(len(st)/PADDING_SIZE)):
            numrep = st[i*PADDING_SIZE:(i*PADDING_SIZE)+PADDING_SIZE]
            mystr = ""
            found = False
            for k,v in self.dic.items():
                if found:
                    break
                else:
                    if v[0] == numrep:
                        mystr = k
                        found = True
            st_elems.append(mystr)
        return st_elems
    
#-----------------------------------------------------------------------build_dict
class NextToken():
    '''
    next_tokens est un dic avec
    key: concaténation des id des tokens, chacun paddé sur 4 char avec leading 0
    value: [
      [padded_token_id, nb_occurence],
      [padded_token_id, nb_occurence],
      etc.
    ]
    Pas besoin du dic, NextToken travaille seulement sur les tokens
    '''
    def __init__(self, window_size):
        self.nex = {}
        self.dic = dic
        self.window = window_size

    def scan(self, tokens):
        for i in range(len(tokens)-self.window):
            # getting the real words
            attention = tokens[i : i+self.window]
            next_t = tokens[i+self.window]
            # converting the key and value to nums based on dic
            key = ""
            for elem in attention:
                key += elem
            value = next_t
            # manage count
            if key not in self.nex:
                self.nex[key] = [[value, 1]]
            else:
                print(f"***** We have one! ***** Attention: {attention}, next token: '{next_t}'")
                # do we have already the value?
                alternates = self.nex[key]
                #breakpoint(f"BEFORE - Alternates: {alternates} - Value: {value}")
                exist = False
                for e in alternates:
                    if e[0] == value:
                        exist = True
                        print("Value already exists")
                        e[1] += 1
                if not exist:
                    alternates.append([value, 1])
                self.nex[key] = alternates
                #breakpoint(f"AFTER - Alternates: {alternates}")
        return True

    def print(self, dic):
        outstr = ""
        for key, value in self.nex.items():
            #showing only singular items
            if len(value) != 1:
                outstr = f"Key: {key} - Value: {value} |"
                for word in dic.decode(key):
                    outstr += f" {word}"
                for elem in value:
                    outstr += f" | {dic.decode(elem[0])[0]} ({str(elem[1])})"
                print(outstr)

    
#------------------------------------------------------------------main
if __name__ == "__main__":
    #test()
    #tokens = mytokenizer('the-verdict.txt')
    words = manual_tokenizer('russian-folk-tales.txt',True)
    dic = WordDict()
    tokens = dic.add_words(words)
    print(dic)
    breakpoint()
    print(tokens)
    breakpoint()
    next4 = NextToken(4)
    next4.scan(tokens)
    next3 = NextToken(3)
    next3.scan(tokens)
    next2 = NextToken(2)
    next2.scan(tokens)
    breakpoint()
    print("-"*20)
    next4.print(dic)
    #print("-"*20)
    #next3.print(dic)
    #print("-"*20)
    #next2.print(dic)
