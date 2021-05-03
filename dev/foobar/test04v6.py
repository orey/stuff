def log(s):
    print s
    return

    
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
        return siz + 1 # +1 then siz steps
    # Particular case 2^n + 1
    if (s.count('1') == 2) and (s[-1] == '1'):
        return siz # -1 then siz -1 steps : siz -1 +1 = siz
    # Particular case 2^n + 3 (0b11)
    if (s.count('1') == 3) and (s[-2:] == '11'):
        return siz + 1 # size -2 + 3 (from 3 to 0)
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


if __name__ ==  "__main__":
    while True:
        log("----------------------------------")
        log("Type 'exit' to exit, '0' to launch many tests ")
        n = raw_input("Number to reduce > ")
        if n == 'exit':
            exit()
        elif n == '0':
            for i in range(1,1000):
                if (solutionbaseline(str(i)) != solution(str(i))):
                    log("Different for: " + str(i) + " - " + str(bin(i)))
        else:
            log("Baseline = " + str(solutionbaseline(str(n))))
            log("Min operations = " + str(solution(str(n))))

