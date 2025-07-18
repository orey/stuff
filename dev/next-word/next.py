from importlib.metadata import version

import tokenize

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
    next_tokens = []
    for i in range(len(tokens)-window):
        attention = tokens[i:i+window]
        next_tokens.append((attention, tokens[i+window]))
    return next_tokens


if __name__ == "__main__":
    #test()
    tokens = mytokenizer('the-verdict.txt')
    dic = build_dict(tokens)
    print(dic)
    print(len(dic))
    next_tokens = scan(tokens, 4, dic)
    print(next_tokens)
    
    

