VERBOSE = True

def log(s):
    print s
    return

def uptopowersup(s):
    siz = len(s)
    powersup = '1' + ('0' * siz)
    p = binString2Long(powersup) - binString2Long(s)
    return p + siz

def downtopowerinf(s):
    siz = len(s)
    powerinf = '1' + ('0' * (siz - 1))
    p = binString2Long(s) - binString2Long(powerinf)
    return p + siz


    
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
        temp1 = uptopowersup(s) + count
        temp2 = downtopowerinf(s) + count
        temp3 = 0L
        # standard reduce
        twofig = s[-2:]
        if twofig == '11':
            # best is to increment because we can divide twice by 2
            temp3 = reduce(long2BinString(binString2Long(s) + 1), count+1)
        else: # '01'
            # best is to decrement to divide twice per 2
            temp3 = reduce(long2BinString(binString2Long(s) - 1), count+1)
        return min(temp1, temp2, temp3)

        
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
        try:
            if n == 'exit':
                exit()
            elif n == 'a':
                VERBOSE = False
                analysis_a()
            elif n == 'b':
                VERBOSE = False
                analysis_b()
            else:
                VERBOSE = True
                print "Baseline = " + str(solutionbaseline(str(n)))
                print "Min operations = " + str(solution(str(n)))
        except Exception:
            print "Unrecognized command"
            continue

