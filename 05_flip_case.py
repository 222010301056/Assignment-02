# pylint: disable=invalid-name
"""
Flip case
Given an alphabetical string s, flip
every uppercase character to lowercase and
every lowercase character to uppercase.

Example 1
Input
s = "binarySEARCH"

Output
"BINARYsearch"

Example 2
Input
s = "GiTaM"

Output
"gItAm"
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def flip_case(s):
    return s.swapcase()




# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable
class TestFlipCase(unittest.TestCase):

    def test_01(self):
        self.assertEqual(flip_case("binarySEARCH"), "BINARYsearch")

    def test_02(self):
        self.assertEqual(flip_case("GiTaM"), "gItAm")

    def test_03(self):
        self.assertEqual(flip_case(""), "")

    def test_04(self):
        self.assertEqual(flip_case("a"), "A")

    def test_05(self):
        self.assertEqual(flip_case("TestFlipCase"), "tESTfLIPcASE")

    def test_06(self):
        self.assertEqual(flip_case("assertEqual"), "ASSERTeQUAL")

    def test_07(self):
        self.assertEqual(flip_case("unittest"), "UNITTEST")

    def test_08(self):
        self.assertEqual(flip_case("cODINGcULTURE"), "CodingCulture")


if __name__ == '__main__':
    unittest.main(verbosity=2)
