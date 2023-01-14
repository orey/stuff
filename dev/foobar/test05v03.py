def log(s):
#    print s
    return

def calc(n, rank, sup):
    log(("    " * rank) + "rank=" + str(rank) + " n=" + str(n) + " sup=" +str(sup))
    result = 0
    if (n == 1) or (n == 2):
        log(("    " * rank) + "No combination")
        return 0
    for i in range(n-1, 1, -1):
        log(("    " * rank) + "i=" + str(i))
        rest = n-i
        if rest > i*(i-1)/2:
            log(("    " * rank) + "No combination")
            continue
        # 2 cols
        if rank == 1:
            print i
            if rest < i:
                result += 1
                log(("    " * rank) + "SOLUTION : rank= "+str(rank)+" i=" + str(i) + " rest=" + str(rest))
        else:
            if rest < i and i < sup:
                result += 1
                log(("    " * rank) + "SOLUTION : rank= "+str(rank)+" i=" + str(i) + " rest=" + str(rest))
        # More colums
        result += calc(rest,rank+1, i)
    return result

def solution(n):
    return calc(n, 1, 0)



if __name__ ==  "__main__":
    while True:
        print "----------------------------------"
        print "Type 'exit' to exit"
        n = raw_input("Number of stairs > ")
        if n == 'exit':
            exit()
        else:
            print "Combinaisons = " + str(solution(int(n)))
        
            
    
