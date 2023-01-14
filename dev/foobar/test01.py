# Using ASCII codes
# f(x) = -x + 219
import unittest

iTEST1 = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
oTEST1 = "did you see last night's episode?"

iTEST2 = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
oTEST2 = "Yeah! I can't believe Lance lost his job at the colony!!"

def decypher(input):
    il = list(input)
    ol = []
    for c in il:
        if ord(c) in range(97,123):
            ol.append(chr(219 - ord(c)))
        else:
            ol.append(c)
    return ''.join(ol)

class TestDecypher(unittest.TestCase):
    def test_test1(self):
        self.assertEqual(decypher(iTEST1),oTEST1)

    def test_test2(self):
        self.assertEqual(decypher(iTEST2),oTEST2)

def solution():
    unittest.main()

