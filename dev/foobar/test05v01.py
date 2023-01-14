def solution(p):
    result = 0
    return reduce(p, 2, result)

def reduce(p, c, result):
    if c == 2:
        # two columns
        if p%2 ==0: #even
            result + p/2 -1
        else: #odd
            result += p//2
    for i in range(c+1,p+1):
        mincol = i*(i+1)/2
        if p < mincol: # no solutions for c columns
            return result
        mintosplit = i*(i-1)/2
        for m in range(mintosplit, p-i):
            return reduce(m, i-1, result)


if __name__ ==  "__main__":
    while True:
        print "----------------------------------"
        print "Type 'exit' to exit"
        n = raw_input("Number of stairs > ")
        if n == 'exit':
            exit()
        else:
            print "Combinaisons = " + str(solution(int(n)))
        
            
    
