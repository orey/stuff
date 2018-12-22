#-------------------------------------------------------------------------------
# Name:        graphtest.py
# Purpose:     Graph transformation implementation
#
# Author:      O. Rey
#
# Created:     September 18 2018
# Copyleft:    GNU GPL v3
#-------------------------------------------------------------------------------
import unittest
from graphtransfo import *

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        #-- test1
        n1 = Node("test", "bateau", 12)
        self.assertIsInstance(n1, Node)
        #-- test2: testing __repr__
        print(n1)
        #-- test3
        try:
            n2 = Node('tst', 'oiseau','toto')
        except TypeError as e:
            self.assertIsInstance(e, TypeError)
            print(e)
        #-- test4
        n2 = Node('tst', 'oiseau', 12)
        self.assertEqual(n1, n2)
        print("Testing equality:", n1 == n2)

if __name__ == '__main__':
    unittest.main()
    
