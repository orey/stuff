def mainPath(n, acc, alternates):
    if n == 2:
        acc.append(1)
        return
    # n even
    if n%2 == 0:
        temp = n/2
        acc.append(temp)
        mainPath(temp, acc, alternates)
        return
    # Choose default path by using -1 operation
    else:
        temp = n-1
        # Deal with alternate: [nb of nodes, start]
        alternates.append([len(acc), n+1])
        # Manage baseline case
        acc.append(temp)
        mainPath(temp, acc, alternates)
        return


def manageAlternates(alternates, l0):
    c = 0
    min = l0
    print "Number of alternates at this level = " + str(len(alternates))
    for a in alternates:
        c = solution(str(a[1])) + a[0]
        print "Alternate solution: " + str(a) + ' - ' +str(c)
        if c < min:
            min = c
    return min


def solution(str):
    # n is a string
    n = long(str)
    acc = [n]
    alternates = []
    mainPath(n, acc, alternates)
    print "=== baseline ==="
    print acc
    print alternates
    l0 = len(acc) - 1
    print "l0 = "
    print l0
    min = manageAlternates(alternates, l0)
    return min


print "Min of 17: " + str(solution("17"))
print "+++++++++++++++++++++++++++++++++"
print "Min of 31: " + str(solution("31"))
print "+++++++++++++++++++++++++++++++++"
print "Min of 18: " + str(solution("18"))
print "+++++++++++++++++++++++++++++++++"
print "Min of 15: " + str(solution("15"))
print "+++++++++++++++++++++++++++++++++"
print "Min of 4: " + str(solution("4"))
print "+++++++++++++++++++++++++++++++++"
#print "Min of big: " + str(solution("123123123"))
print "Min of 64: " + str(solution("63"))
    
