import math

VERBOSE = True

def log(s):
    print s
    return

def analyze(s):
    if s == '1':
        return 0
    if s == '10':
        return 1
    if s == '11' or s == '100':
        return 2
    if s == '101' or s == '110':
        return 3
    if s == '111':
        return 4
    siz = len(s)

    # determine k: 2^(k-1) < n < 2^k
    k = 0
    powerup = 0
    powerdown = 0
    n = binString2Long(s)
    log("=== Powers of 2 ===")
    if s.count('1') == 1:
        log(str(binString2Long(s)) + " = 2^" + str(siz))
        k = siz
    else:
        log("2^" + str(siz-1) + " < " + str(n) + " < 2^" + str(siz))
        k = siz
        sup = math.pow(2,k)
        inf = math.pow(2,k-1)
        powerup = sup - n
        powerdown = n - inf
        log("Power of 2 intervals: [<-" + str(powerdown) + "--" + str(n) + "--" + str(powerup) + "->]")
        margin = k//2 - 1 # see approximation
        if n >= sup-margin: # n<sup
            log("=> Converge to powerup. min = " + str(k+ powerup))
            return k + powerup
        margin = (k-1)//2 -1
        if n <= inf+margin: #inf<n
            log("=> Converge to powerdown. min = " + str(k-1+ powerdown))
            return k-1+ powerdown

    for i in range(2,siz-2): # siz-1 is exact 2^k
        log("=== Placement on "+str(math.pow(2,i)) +" multiples ===")
        lastdig = s[-i:]
        iup = 0
        idown = 0
        if lastdig == '0' * i:
            log("Already a multiple of " + str(math.pow(2,i)))
        else:
            inf = binString2Long(s[0:siz-i] + ('0'*i))
            idown = n - inf
            sup = inf + math.pow(2,i)
            iup = sup - n
            log(str(inf) + " < " + str(n) + " < " + str(sup))
            log(str(math.pow(2,i)) + " multiple intervals: [<-" + str(idown) + "--" + str(n) + "--" + str(iup) + "->]")
    

    
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

    
def binString2Long(s):
    return long('0b' + s, 2)


def long2BinString(lo):
    return str(bin(lo))[2:]


def reduce(s, count):
    if VERBOSE:
        log("reduce : " + s + " - " + str(count))
    siz = len(s)
    # End of the loop
    if siz == 1:
        return count
    if s == '10':
        return count + 1
    # 3 (0b11) is irregular
    if s == '11':
        return count + 2
    # Particular case 2^n - 1
    if s.count('0') == 0:
        return count + siz + 1 # +1 then siz steps
    # Particular case 2^n + 1
    if (s.count('1') == 2) and (s[-1] == '1'):
        return count + siz # -1 then siz -1 steps : siz -1 +1 = siz
    # Particular case 2^n + 3 (0b11)
    if (siz > 3) and (s.count('1') == 3) and (s[-2:] == '11'):
        return count + siz + 1 # size -2 + 3 (from 3 to 0)
    # Even
    if s[-1] == '0':
        # divide by 2
        count += 1
        return reduce(s[0:siz-1], count)
    else:
        # Odd
        twofig = s[-2:]
        count += 1
        if twofig == '11':
            # best is to increment because we can divide twice by 2
            return reduce(long2BinString(binString2Long(s) + 1), count)
        else: # '01'
            # best is to decrement to divide twice per 2
            return reduce(long2BinString(binString2Long(s) - 1), count)

        
def solution(str):
    n = long(str)
    if n == 1:
        return 0
    count = 0
    return reduce(long2BinString(n), count)


def solutionbaseline(str):
    n = long(str)
    if n == 1:
        return 0
    count = 0
    return baseline(long2BinString(n), count)


def analysis_a():
    for i in range(1,1000):
        b = solutionbaseline(str(i))
        s = solution(str(i))
        if (b != s):
            log("For " + str(i) + " - " + str(bin(i)) + " : [B:" + str(b) + "][Min:" + str(s) + "]")
        else:
            log("For " + str(i) + " - " + str(bin(i)) + " : [B:" + str(b) + "]")

def analysis_b():
    for i in range(1,1000000):
        b = solutionbaseline(str(i))
        s = solution(str(i))
        if (b < s):
            log("For " + str(i) + " - " + str(bin(i)) + " : [B:" + str(b) + "][Min:" + str(s) + "]")        



if __name__ ==  "__main__":
    while True:
        print "----------------------------------"
        print "Type 'exit' to exit, 'a' to launch analysis "
        n = raw_input("Number to reduce > ")
        #try:
        if n == 'exit':
            exit()
        elif n == 'a':
            VERBOSE = False
            analysis_a()
        elif n == 'b':
            VERBOSE = False
            analysis_b()
        elif n.startswith('c '):
            l = n.split(' ')
            analyze(long2BinString(long(l[1])))
        else:
            VERBOSE = True
            print "Baseline = " + str(solutionbaseline(str(n)))
            print "Min operations = " + str(solution(str(n)))
        #except Exception as e:
        #    print "Unrecognized command"
        #    print e
        #    continue

