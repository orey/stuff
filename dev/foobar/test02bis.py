SUP = 100000

def solution(x, y):
    if not ((x >=1) and (y >=1) and (x <= SUP) & (y <= SUP)):
        #raise ValueError("Value should be at least 1 and at most 100,000")
        return -1
    # Calculating diagonal rank
    r = (x + y -1)
    # Calculating last index in previous rank
    n = r - 1
    lastindex = (n+1)*n/2
    return str(lastindex + x)

print solution(3,2)
print solution(5,10)
