VERBOSE = True

def log(s):
    if VERBOSE:
        print s
    return

def binString2Long(s):
    return long('0b' + s, 2)

def long2BinString(lo):
    return str(bin(lo))[2:]

def baseline(s, count, alternates):
    siz = len(s)
    if siz == 1:
        return count
    if s == "10":
        return count + 1
    if s == "11":
        return count + 2
    if s[-1] == '0':
        # divide by 2
        count += 1
        return baseline(s[0:siz-1], count, alternates)
    else: # last figure is 1 and siz >= 3
        # capture alternate +1
        temp = long2BinString(binString2Long(s) + 1)
        alternates.append([temp, count + 1])
        # manage baseline case -1
        count +=1
        return baseline(s[0:siz-1] + '0', count, alternates)


def manageAlternates(alternates, count):
    mini = count
    log("Alternates: " + str(alternates))
    print "Alternates: " + str(alternates)
    if (alternates == None) or (len(alternates) == 0):
        return mini
    for a in alternates:
        log("--- Treating: " + str(a))
        temp = solution(str(binString2Long(a[0]))) + a[1]
        if temp < mini:
            mini = temp
    return mini

    
def solution(s):
    # s is a string
    n = long(s)
    if n == 1:
        return 0
    log("Provided number: " + str(bin(n)))
    count = 0
    alternates = []
    countbis = baseline(long2BinString(n), count, alternates)
    log("Baseline = " + str(countbis))
    if len(alternates) != 0:
        min = manageAlternates(alternates, countbis)
        log("Min = " + str(min))
        return min
    else:
        log("Min = " + str(countbis))
        return countbis


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
