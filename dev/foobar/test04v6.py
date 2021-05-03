def binString2Long(s):
    return long('0b' + s, 2)

def long2BinString(lo):
    return str(bin(lo))[2:]

def reduce(s, count):
    print "reduce : " + s + " - " + str(count)
    siz = len(s)
    # End of the loop
    if siz == 1:
        return count
    if s == '10':
        return count + 1
    if s == '11':
        return count + 2
    # Particular case 2^n - 1
    if s.count('0') == 0:
        return siz + 1 # +1 then siz steps
    # Particular case 2^n + 1
    if (s.count('1') == 1) and (s[-1] == '1'):
        return siz # -1 then siz -1 steps : siz -1 +1 = siz
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

if __name__ ==  "__main__":
    while True:
        print "Type 0 to exit"
        n = input("Number to reduce: ")
        if n == 0:
            exit()
        # n is already a string
        print "Min operations = " + str(solution(n))

