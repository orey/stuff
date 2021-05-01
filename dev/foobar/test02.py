import unittest

SUP = 100000

# Imposed tests
TEST1 = [3, 2, '9']
TEST2 = [5, 10, '96']

# Personal tests
TEST3 = [1, 1, '1']
TEST4 = [2, 3, '8']

TEST5 = [-1, 12]
TEST6 = [22, 120000]
TEST7 = [100001, 12]
TEST8 = [22, 0]


def solution(x, y):
    if not ((x >=1) and (y >=1) and (x <= SUP) & (y <= SUP)):
        raise ValueError("Value should be at least 1 and at most 100,000")
    # Calculating diagonal rank
    r = (x + y -1)
    # Calculating last index in previous rank
    n = r - 1
    lastindex = (n+1)*n/2
    return str(lastindex + x)
    
class TestIds(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(solution(TEST1[0], TEST1[1]), TEST1[2])
        self.assertEqual(solution(TEST2[0], TEST2[1]), TEST2[2])
        self.assertEqual(solution(TEST3[0], TEST3[1]), TEST3[2])
        self.assertEqual(solution(TEST4[0], TEST4[1]), TEST4[2])

    def test_errors(self):
        self.assertRaises(ValueError, solution, (TEST5[0], TEST5[1]), None)
        self.assertRaises(ValueError, solution, (TEST6[0], TEST6[1]), None)
        self.assertRaises(ValueError, solution, (TEST7[0], TEST7[1]), None)
        self.assertRaises(ValueError, solution, (TEST8[0], TEST8[1]), None)
    
unittest.main()

