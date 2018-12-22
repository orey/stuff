#-------------------------------------------------------------------------------
# Name:        graphtransfo.py
# Purpose:     Graph transformation implementation
#
# Author:      O. Rey
#
# Created:     September 16 2018
# Copyleft:    GNU GPL v3
#-------------------------------------------------------------------------------

ERR_MSG = { 0 : "TypeError: ID must be an integer", \
            1 : "TypeError: Node can only compare to Node" }

class Node:
    def __init__(self, domain, ntype, ID):
        self.domain = domain
        self.ntype = ntype
        if not type(ID) == int:
            raise TypeError(ERR_MSG[0])
        self.ID = ID
        self.attributes = {}
    def __hash__(self):
        return ID
    def __eq__(self, other):
        if not type(other) == Node:
            raise TypeError(ERR_MSG[1])
        if other.ID == self.ID:
            return True
        else:
            return False
    def __repr__(self):
        return "Node - domain=" + self.domain + ", type=" + \
               self.ntype + ", ID=" + str(self.ID) + \
               ", attributes=" + str(self.attributes)                

        
class Graph:
    def __init__(self, name):
        self.name = name
        self.nodes = {}
        
if __name__ == "__main__":
    test_node()
    
