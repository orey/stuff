from importlib.metadata import version

import tokenize
import sys

import re

#TO_REMOVE = []


def test():
    '''
    Avec le basic tokenizer "Gisburn's painting" le "'s" ne passe pas.
    '''
    line = ""
    with tokenize.open('the-verdict.txt') as f:
        try:
            line = f.readline
            tokens = tokenize.generate_tokens(line)
            for token in tokens:
                print(token)
        except Exception as e:
            print(e)
            print(f"Incriminated line:\n---\n{line}\n---\n")

def mytokenizer(f):
    '''
    Test avec les re
    '''
    with open(f) as g:
        text = g.read()
        tokens = re.findall(r'\w+', text)
        print(tokens)
        return tokens

def build_dict(tokens):
    '''
    dict key : token
    dict value : [integer_representation, nb_occurences]
    '''
    dic = {}
    count = 0
    for token in tokens:
        if token in dic:
            rep = dic[token][0]
            occ = dic[token][1]
            dic[token] = [rep, occ+1]
        else:
            dic[token] = [count+1, 1]
            count +=1
    return dic


def scan(tokens, window, dic):
    '''
    next_tokens est un dic avec
    key: concaténation des id des tokens, chacun paddé sur 4 char avec leading 0
    value: [ [padded token id, nb occurence], [padded token id, nb occurence], etc. ]
    '''
    next_tokens = {}
    for i in range(len(tokens)-window):
        # getting the real words
        attention = tokens[i:i+window]
        next = tokens[i+window]
        # converting the key and value to nums based on dic
        key = ""
        for elem in attention:
            # We pad elements to 4 with leading 0 because the dic is of size 1137
            key += str("{:04d}".format(dic[elem][0]))
        value = "{:04d}".format(dic[tokens[i+window]][0])
        #breakpoint(f"Attention: {attention} - Next: {next}\nKey: {key} - Value: {value}")
        # manage count
        if key not in next_tokens:
            next_tokens[key] = [[value, 1]]
        else:
            print("***** We have one! *****")
            print(f"Attention: {attention}, next token: '{next}'")
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
    return next_tokens

def smart_print(next_tokens, window, dic):
    print("Printing only the singular items:")
    for key, value in next_tokens.items():
        if len(value) != 1:
            print(f"Key: {key} - Value: {value}")
            decode(dic, key, window, value)


def breakpoint(obj):
    print(obj)
    a = input("Do you want to continue? ('n' will stop) ")
    if a == "n":
        print("Goodbye")
        sys.exit()
    


def decode(dic, key, window, value):
    key_elems = []
    for i in range(int(len(key)/4)):
        numrep = int(key[i*4:(i*4)+4])
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
        numrep = int(elem[0])
        mystr = ""
        for k,v in dic.items():
            if v[0] == numrep:
                mystr = k
                break;
        possibles.append(mystr)
    print(f"Key: {key_elems} - Possible next: {possibles}")
        


if __name__ == "__main__":
    #test()
    tokens = mytokenizer('the-verdict.txt')
    dic = build_dict(tokens)
    print(dic)
    print(len(dic))
    window = 3
    next_tokens = scan(tokens, window, dic)
    smart_print(next_tokens, window, dic)
    window = 4
    next_tokens = scan(tokens, window, dic)
    smart_print(next_tokens, window, dic)
    
    

