PLUS = '+'
MINUS = '-'
DIVIDE = '/'


# lin : [level, [n, previousops]]
def reduce(lin):
    level = lin[0]
    siz = len(lin)
    lout = [level+1]
    for i in range(1, siz):
        olde_n = lin[i][O]
        if olde_n == 1:
            continue
        olde_o = lin[i][1]
        # if n even 3 possibilities
        if olde_n%2 == 0:
            lout.append([])
        
        
        
        
        
    
