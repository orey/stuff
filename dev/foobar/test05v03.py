def log(s):
    print s
    return

def calc(n, rank, sup):
    result = 0
    if (n == 1) or (n == 2):
        return 0
    for i in range(n-1, 1, -1):
        rest = n-i
        # 2 cols
        if rank == 1:
            if rest < i:
                result += 1
        else:
            if rest <i and i < sup:
                result += 1
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
        
            
    
