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
    for a in alternates:
        c = solution(str(a[1])) + a[0]
        if c < min:
            min = c
    return min


def solution(str):
    # n is a string
    n = long(str)
    acc = [n]
    alternates = []
    mainPath(n, acc, alternates)
    l0 = len(acc) - 1
    min = manageAlternates(alternates, l0)
    return min


