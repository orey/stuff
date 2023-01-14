def log(s):
    print s
    return

def solution(p):
    result = 0
    for c in range(2,p):
        result += reduce(p, c)
    return result

def reduce(p, c):
    if c == 2:
        # two columns
        if p%2 ==0: #even
            return p/2 -1
        else: #odd
            return p//2
    mincol = c*(c+1)/2
    if p < mincol: # no solutions for c columns
        log('No solution for columns ' + str(c)) 
        return 0
    mintosplit = c*(c-1)/2
    temp = 0
    for m in range(mintosplit, p-c):
        temp += reduce(m, c-1)
    return temp


if __name__ ==  "__main__":
    while True:
        print "----------------------------------"
        print "Type 'exit' to exit"
        n = raw_input("Number of stairs > ")
        if n == 'exit':
            exit()
        else:
            print "Combinaisons = " + str(solution(int(n)))
        
            
    
