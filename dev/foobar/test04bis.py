INCREMENT = 0

def createId():
    INCREMENT +=1
    return INCREMENT
    

class Node:
    def __init__(self, value):
        print "Node created: " + str(value)
        self.id = createId()
        self.value = value
        # for /2 operation or -1 if odd
        self.next1 = None
        # for +1 operation if odd
        self.next2 = None
        self.previous = None

    def setNext1(self, value):
        self.next1 = value
        
    def setNext2(self, value):
        self.next2 = value

    def setPrevious(self, value):
        self.previous = value

    def getNext1(self):
        return self.next1

    def getNext2(self):
        return self.next2

    def getValue(self):
        return self.value

    def getId(self):
        return self.id

    def nprint(self):
        if self.next1 != None:
            print '[' + str(self.value) + '|NEXT1:' + str(self.next1.value) + ']'
        else:
            print '[' + str(self.value) + ']'

NEXT1 = 1
NEXT2 = 2
PREVIOUS = 0
        
class Tree:
    def __init__(self, node):
        node = Node(value)
        self.dico = {node.getId():node}

    def append(self, node, previousvalue):
        self.dico[node.getId()] = node
        temp = self.cursor
        if which == NEXT1:
            temp.setNext1(node)
        else:
            temp.setNext2(node)
        node.setPrevious(temp)
        self.cursor = node

    def nprint(self):
#        node = self.tree[0]
#        print "Debut de nprint : " + str(node.value)
#        while node != None :
#            node.nprint()
#            node = node.getNext1()
        print "--------------"
        for e in self.tree:
            e.nprint()


def mainPath(n, acc):
    if n == 2:
        acc.nappend(Node(1), NEXT1)
        return acc
    # n even
    if n%2 == 0:
        temp = n/2
        acc.nappend(Node(temp), NEXT1)
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
    acc = Tree(Node(n))
    outacc = mainPath(n, acc)
    # to remove
    outacc.nprint()
    # return len(outacc) - 1

# to remove
print solution("17")
print solution("31")

    
