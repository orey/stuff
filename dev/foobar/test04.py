def mainPath(n, acc):
    if n == 2:
        acc.append(1)
        return acc
    # n even
    if n%2 == 0:
        temp = n/2
        acc.append(temp)
        return mainPath(temp, acc)
    # Choose default path by using -1 operation
    else:
        temp = n-1
        acc.append(temp)
        return mainPath(temp, acc)
    
def solution(str):
    # n is a string
    n = long(str)
    acc = [n]
    outacc = mainPath(n, acc)
    # to remove
    print outacc
    return len(outacc) - 1

# to remove
print solution("17")
print solution("31")

    
