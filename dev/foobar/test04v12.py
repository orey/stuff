VERBOSE = True

def log(s):
    print s
    return

def binString2Long(s):
    return long('0b' + s, 2)

def long2BinString(lo):
    return str(bin(lo))[2:]

def reduce(level, levels, alln):
    temp = []
    listlevel = levels[level -1]
    for n in listlevel:
        siz = len(n)
        if n == '1':
            return level # end of recursive loop
        if n[-1] == 0: # even
            c = n[0:siz-1]
            if c not in alln:
                alln.append(c)
                temp.append(c)
        else:
            d = n[0:siz-1] + '0' # -1
            e = long2BinString(binString2Long(n) + 1)
            if d not in alln:
                alln.append(d)
                temp.append(d)
            if e not in alln:
                alln.append(e)
                temp.append(e)
    levels[level] = temp
    #return reduce(level+1, levels, alln)
    log(levels)
    log(alln)
                
            
            
            


def solution(s):
    n = long2BinString(long(s))
    log("Binary number provided: " + str(n))
    levels = {0:[n]}
    alln = [n]
    level = 1
    reduce(level, levels, alln)
    
    
    
    

### BASELINE
def solutionbaseline(str):
    n = long(str)
    if n == 1:
        return 0
    count = 0
    return baseline(long2BinString(n), count)

def baseline(s, count):
    siz = len(s)
    if siz == 1:
        return count
    if s[-1] == '0':
        # divide by 2
        count += 1
        return baseline(s[0:siz-1], count)
    else:
        # -1
        count +=1
        return baseline(s[0:siz-1] + '0', count)


if __name__ ==  "__main__":
    while True:
        print "----------------------------------"
        print "Type 'exit' to exit"
        n = raw_input("Number to reduce > ")
        #try:
        if n == 'exit':
            exit()
        else:
            VERBOSE = True
            print "Baseline = " + str(solutionbaseline(str(n)))
            print "Min operations = " + str(solution(str(n)))
        #except Exception:
        #    print "Unrecognized command"
        #    continue
