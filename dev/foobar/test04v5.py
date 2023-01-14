import math

def intervals(n, count):
    binn = bin(n)
    # lowest power of 2
    l = len(binn) - 3
    # exact power of 2
    if binn.count('1') == 1:
        return l + count    
    left = n - pow(2, l)
    right = pow(2, l+1) - n
    if right + 1 < left:
        return l + right + 1
    else:
        return l + left
    


def even(n, count):
    


def solution(str):
    # n is a string
    n = long(str)
    if n == 1:
        return 0


print "solution(4096): " + str(solution("4096"))
print "solution(4095): " + str(solution("4095"))
#print "solution(2): " + str(solution("2"))
#print "solution(3): " + str(solution("3"))
#print "solution(17): " + str(solution("17"))
#print "solution(15): " + str(solution("15"))
#print "solution(4): " + str(solution("4"))

