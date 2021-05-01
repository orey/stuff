LEFT = '<'
RIGHT = '>'

#         01234567891234
SAMPLE = "--->-><-><-->-"


class Employee:
    def __init__(self, pos, d, hw):
        self.pos = pos
        self.d = d
        self.hw = hw
        
    def move(self):
        if self.d == LEFT:
            self.pos -= 1
        else:
            self.pos += 1
        # See if employee still in hallway
        if (self.pos < 0) or (self.pos >= self.hw):
            return False
        else:
            return True

    def getBinaryPosition(self):
        temp = '0' * self.hw
        temp2 = temp[0:self.pos] + '1' + temp[self.pos+1:]
        return int(temp2, 2)

    def view(self):
        print bin(self.getBinaryPosition()) + " " + self.d


class Hallway:
    def __init__(self, descr):
        self.descr = descr
        self.length = len(descr)
        self.lefties = []
        self.righties = []
        # create employees at their initial positions
        r = range(self.length)
        for i in r:
            c = descr[i]
            if c == '-':
                continue
            elif c == LEFT:
                self.lefties.append(Employee(i, LEFT, self.length))
            elif c == RIGHT:
                self.righties.append(Employee(i, RIGHT, self.length))
            else:
                raise ValueError("Unknown character")
        self.salutes = 0

    def moveOneRound(self):
        if (len(self.lefties) == 0) or (len(self.righties) == 0):
            return False
        for e in self.lefties:
            if not e.move():
                self.lefties.remove(e)
        if len(self.lefties) == 0:
            return False
        else:
            self.countSalutes()
        print self.lefties
        for e in self.righties:
            if not e.move():
                self.righties.remove(e)
        if len(self.righties) == 0:
            return False
        else:
            self.countSalutes()
        print self.righties
        print "----------------"
        return True

    def countSalutes(self):
        l = []
        for e in self.lefties:
            l.append(e.getBinaryPosition())
        for e in self.righties:
            l.append(e.getBinaryPosition())
        self.view()
        r = reduce(lambda x,y: x & y, l)
        ct = bin(r).count('1')
        self.salutes += ct

    def getSalutes(self):
        return self.salutes

    def view(self):
        print '-------------------'
        for e in self.lefties:
            e.view()
        for e in self.righties:
            e.view()
    
        
def solution(descr):
    h = Hallway(descr)
    while h.moveOneRound():
        continue
    print h.getSalutes()
        
solution(SAMPLE)
        
            
            
                

    
    

