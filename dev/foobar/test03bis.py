LEFT = '<'
RIGHT = '>'
VOID = '-'

SAMPLE = "--->-><-><-->-"
TEST1 = ">----<"
TEST2 = "<<>><"

def countLeft(str):
    r = range(len(str))
    count = 0
    for i in r:
        if str[i] == LEFT:
            count += 1
    return count

def solution(str):
    r = range(len(str))
    count = 0
    for i in r:
        if str[i] == RIGHT:
            count += countLeft(str[i:])
    return count*2

print solution(SAMPLE)
print solution(TEST1)
print solution(TEST2)

