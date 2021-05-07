from datetime import datetime

def log(s):
    print s
    return

def calc(n, rank, sup, soluces):
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
            if rest < i:
                result += 1
                log(("    " * rank) + "SOLUTION : rank= "+str(rank)+" i=" + str(i) + " rest=" + str(rest))
        else:
            if rest < i and i < sup:
                result += 1
                log(("    " * rank) + "SOLUTION : rank= "+str(rank)+" i=" + str(i) + " rest=" + str(rest))
        # More colums
        usesoluces = False
        #log(soluces)
        for s in soluces:
            if s[0] == rest and s[1] == rank+1:
                log(("    " * rank) + "Reused from soluces")
                result += s[2]
                usesoluces = True
                break;
        if not usesoluces:
            result += calc(rest, rank+1, i, soluces)
    if [n, sup, result] not in soluces:
        soluces.append([n, sup, result])
    return result

def solution(n):
    # [[n, sup, value], ... ]
    soluces = [[1,0,0],[2,0,0]]
    start = datetime.now()
    a = calc(n, 1, 0, soluces)
    log("Elapse time=" +str(datetime.now() -start))
    print soluces
    return a



if __name__ ==  "__main__":
    while True:
        print "----------------------------------"
        print "Type 'exit' to exit"
        n = raw_input("Number of stairs > ")
        if n == 'exit':
            exit()
        else:
            print "Combinaisons = " + str(solution(int(n)))
        
            
    
