# R1: even - divide by 2 - remove a zero in binary : 1 op
# R2a: odd - minus 1 : 1 op
# R2b: odd - for n given, n + p = 2^k :  p+k op
# R2c: odd - for n given, n - p = 2^k :  p+k op
# for n close to 2^k and inferior R2b is better than R2a
# R3: 2^k-1 : k+1 op
VERBOSE = True

def log(s):
    if VERBOSE:
        print s
    return

def binString2Long(s):
    return long('0b' + s, 2)

def long2BinString(lo):
    return str(bin(lo))[2:]

def ruleR2b(s):
    siz = len(s)
    powersup = '1' + ('0' * siz)
    p = binString2Long(powersup) - binString2Long(s)
    return p + siz

def ruleR2c(s):
    siz = len(s)
    powersup = '1' + ('0' * (siz - 1))
    p = binString2Long(s) - binString2Long(powersup)
    return p + siz

def baseline(s, count):
    '''
    This function implements a baseline based on R1 and R2a
    '''
    siz = len(s)
    if siz == 1:
        return count
    # R3 2^n - 1
    if (s.count('0') == 0) and (siz >2):
        return count + siz + 1
    if s[-1] == '0':
        # Even R1
        return baseline(s[0:siz-1], count+1)
    else:
        # Odd R2a
        r2a = baseline(s[0:siz-1] + '0', count+1)
        # Odd R2b
        r2b = ruleR2b(s)
        # Odd R2c
        r2c = ruleR2c(s)
        log("[R2a:" + str(r2a) + "][R2b:" + str(r2b) + "][R2c:" + str(r2c) + "]")
        return count + min(r2a, r2b, r2c)

def solution(s):
    # s is a string
    n = long(s)
    if n == 1:
        return 0
    log("Provided number: " + str(bin(n)))
    count = 0
    return baseline(long2BinString(n), count)


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
            for i in range(1,1000):
                print "Number: " + str(i) + " - " + str(bin(i)) + " - " + str(solution(str(i)))
        else:
            VERBOSE = True
            print "The minimal is: " + str(solution(n))
        #except Exception:
        #    print "Unrecognized command"
        #    continue
