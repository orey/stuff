def binString2Long(s):
    return long('0b' + s, 2)

def long2BinString(lo):
    return str(bin(lo))[2:]

def reduce(s, count):
    siz = len(s)
    # End of the loop
    if siz == 1:
        return count
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
    n = input("Number to reduce: ")
    print "Min operations = " + str(solution(str(n)))
    
