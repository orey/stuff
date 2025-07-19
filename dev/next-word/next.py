from importlib.metadata import version

import tokenize
import sys

import re

ADD_SPACE_AROUND = [".",",",";",":","!","?","'",'"',"-","(",")","—"]
REPLACE_BY_SPACE = ["\n", "_"]

#----------------------------------------------------------------------breakpoint
def breakpoint(obj):
    print(obj)
    a = input("Do you want to continue? ('n' will stop) ")
    if a == "n":
        print("Goodbye")
        sys.exit()
    

#-----------------------------------------------------------------------basic_tokenizer
def basic_tokenizer():
    '''
    Avec le basic tokenizer "Gisburn's painting" le "'s" ne passe pas.
    '''
    line = ""
    with tokenize.open('the-verdict.txt', encoding="utf-8") as f:
        try:
            line = f.readline
            tokens = tokenize.generate_tokens(line)
            for token in tokens:
                print(token)
        except Exception as e:
            print(e)
            print(f"Incriminated line:\n---\n{line}\n---\n")

            
#-----------------------------------------------------------------------regex_tokenizer
def regex_tokenizer(f):
    '''
    Test avec les re
    '''
    with open(f) as g:
        text = g.read()
        tokens = re.findall(r'\w+', text)
        print(tokens)
        return tokens


#-----------------------------------------------------------------------manual_tokenizer
def manual_tokenizer(f, verbose = False):
    '''
    More basic stuff
    '''
    with open(f) as g:
        text = g.read()[1:] #removing first char \ufeff
        if verbose: print("Text read")
        text = text.lower()
        if verbose: print("Text in lower case")
        for char in REPLACE_BY_SPACE:
            text = text.replace(char," ")
            if verbose: print(f"{char} removed")
        for char in ADD_SPACE_AROUND:
            text = text.replace(char," " + char + " ")
            if verbose: print("Created spaces around << " + char + " >>")
        return [x for x in text.split(" ") if x] #removing empty strings


#-----------------------------------------------------------------------build_dict    
def build_dict(words, verbose = False):
    '''
    dict key : word
    dict value : [
        string padded of integer_representation (auto-increment counter),
        nb_occurences of the word in the text
    ]
    '''
    padding_size = 4 #dic should not have more than 9999 words
    dic = {}
    count = 0
    tokenized_words = []
    for word in words:
        if word in dic:
            rep = dic[word][0]
            tokenized_words.append(rep)
            occ = dic[word][1]
            dic[word] = [rep, occ+1]
        else:
            rep = ("{:0"+ str(padding_size)+"d}").format(count+1)
            tokenized_words.append(rep)
            dic[word] = [rep, 1]
            count +=1
    if verbose:
        print(f"Dictionary of {len(dic)} words\n{dic}\n")
        #print(f"Tokenized words:\n{tokenized_words}")
        breakpoint("On fait une pause!")
    return dic, tokenized_words


#-----------------------------------------------------------------------build_dict    
def scan(tokens, window, dic):
    '''
    next_tokens est un dic avec
    key: concaténation des id des tokens, chacun paddé sur 4 char avec leading 0
    value: [ [padded_token_id, nb_occurence], [padded_token_id, nb_occurence], etc. ]
    '''
    next_tokens = {}
    for i in range(len(tokens)-window):
        # getting the real words
        attention = tokens[i:i+window]
        next_t = tokens[i+window]
        # converting the key and value to nums based on dic
        key = ""
        for elem in attention:
            key += elem
        value = next_t
        # manage count
        if key not in next_tokens:
            next_tokens[key] = [[value, 1]]
        else:
            print(f"***** We have one! ***** Attention: {attention}, next token: '{next_t}'")
            # do we have already the value?
            alternates = next_tokens[key]
            #breakpoint(f"BEFORE - Alternates: {alternates} - Value: {value}")
            exist = False
            for e in alternates:
                if e[0] == value:
                    exist = True
                    print("Value already exists")
                    e[1] += 1
            if not exist:
                alternates.append([value, 1])
            next_tokens[key] = alternates
            #breakpoint(f"AFTER - Alternates: {alternates}")
    breakpoint(next_tokens)
    return next_tokens


#----------------------------------------------------------------------smart_sprint
def smart_print(next_tokens, window, dic):
    print("Printing only the singular items:")
    for key, value in next_tokens.items():
        if len(value) != 1:
            print(f"Key: {key} - Value: {value}")
            decode(dic, key, window, value)


#----------------------------------------------------------------------decode
def decode(dic, key, window, value):
    key_elems = []
    for i in range(int(len(key)/4)):
        numrep = key[i*4:(i*4)+4]
        #breakpoint(f"{i} - {numrep}")
        mystr = ""
        found = False
        for k,v in dic.items():
            if found:
                break
            else:
                if v[0] == numrep:
                    mystr = k
                    found = True
        key_elems.append(mystr)
        #breakpoint(key_elems)
    possibles = []
    for elem in value:
        numrep = elem[0]
        mystr = ""
        for k,v in dic.items():
            if v[0] == numrep:
                mystr = k
                break;
        possibles.append(mystr)
    print(f"Key: {key_elems} - Possible next: {possibles}")


#-------------------------------------------------------------------next_word
def next_word(window_tokens, next_tokens):
    '''
    window should be a consolidated token list
    '''
    #reprendre ici
    return next_tokens
    

#------------------------------------------------------------------main
if __name__ == "__main__":
    #test()
    #tokens = mytokenizer('the-verdict.txt')
    words = manual_tokenizer('russian-folk-tales.txt',True)
    dic, tokens = build_dict(words,True)
    #window = 3
    #next_tokens = scan(tokens, window, dic)
    #smart_print(next_tokens, window, dic)
    window_size = 4
    next_tokens = scan(tokens, window_size, dic)
    smart_print(next_tokens, window_size, dic)
    
    

