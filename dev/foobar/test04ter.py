# Chose struct is dict {value:previous}


class Node:
    def __init__(self, value):
        print "Node created: " + str(value)
        self.value = value
        # for /2 operation or -1 if odd
        self.next1 = None
        # for +1 operation if odd
        self.next2 = None
        self.previous = None

    def nprint(self):
        print '[' + str(self.value) + '|NEXT1:' + str(self.next1.value) + ']'

NEXT1 = 1
NEXT2 = 2
PREVIOUS = 0
        
class Tree:
    def __init__(self, value):
        node = Node(value)
        self.tree = [node]
        self.cursor = node

    def nappend(self, node, which):
        self.tree.append(node)
        temp = self.cursor
        if which == NEXT1:
            temp.next1 = node
        else:
            temp.next2 = node
        node.previous = temp
        self.cursor = node

    def nprint(self):
        node = self.tree[0]
        print "Debut de nprint : " + str(node.value)
        while node != None :
            node.nprint()
            node = node.next1


def mainPath(n, acc):
    if n == 2:
        acc[1] = 2
        return acc
    # n even
    if n%2 == 0:
        temp = n/2
        acc[temp] = 
        return mainPath(temp, acc)
    # Choose default path by using -1 operation
    else:
        temp = n-1
        acc.nappend(Node(temp), NEXT1)
        acc.nappend(Node(n+1), NEXT2)
        return mainPath(temp, acc)
    
def solution(str):
    # n is a string
    n = long(str)
    acc = [n]
    outacc = mainPath(n, acc)
    # to remove
    outacc.nprint()
    # return len(outacc) - 1

# to remove
print solution("17")
print solution("31")

    
