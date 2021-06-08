# pylint: disable=invalid-name
"""
Multiplication Table
Given an integer n, return a two dimensional matrix representing
an n by n multiplication table. For example, given n=3, return

1 2 3
2 4 6
3 6 9

Example 1
Input
n = 5

Output
[[1, 2, 3, 4, 5],
[2, 4, 6, 8, 10],
[3, 6, 9, 12, 15],
[4, 8, 12, 16, 20],
[5, 10, 15, 20, 25]]
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def multiplication_table(n):
    a=n+1
    table = [[a] * (a-1) for _ in range(a-1)]
    for i in range(1, a):
        for j in range(1, a):
            table[i-1][j-1] = i*j
    return table



# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable,bad-continuation,line-too-long
class TestMultiplicationTable(unittest.TestCase):

    def test_01(self):
        self.assertEqual(multiplication_table(5), [[1, 2, 3, 4, 5],
                                                   [2, 4, 6, 8, 10],
                                                   [3, 6, 9, 12, 15],
                                                   [4, 8, 12, 16, 20],
                                                   [5, 10, 15, 20, 25]])

    def test_02(self):
        self.assertEqual(multiplication_table(1), [[1]])

    def test_03(self):
        self.assertEqual(multiplication_table(0), [])

    def test_04(self):
        self.assertEqual(multiplication_table(11), [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                                                    [2, 4, 6, 8, 10, 12,
                                                        14, 16, 18, 20, 22],
                                                    [3, 6, 9, 12, 15, 18,
                                                        21, 24, 27, 30, 33],
                                                    [4, 8, 12, 16, 20, 24,
                                                        28, 32, 36, 40, 44],
                                                    [5, 10, 15, 20, 25, 30,
                                                        35, 40, 45, 50, 55],
                                                    [6, 12, 18, 24, 30, 36,
                                                        42, 48, 54, 60, 66],
                                                    [7, 14, 21, 28, 35, 42,
                                                        49, 56, 63, 70, 77],
                                                    [8, 16, 24, 32, 40, 48,
                                                        56, 64, 72, 80, 88],
                                                    [9, 18, 27, 36, 45, 54,
                                                        63, 72, 81, 90, 99],
                                                    [10, 20, 30, 40, 50, 60,
                                                        70, 80, 90, 100, 110],
                                                    [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121]])

    def test_05(self):
        self.assertEqual(multiplication_table(7), [[1, 2, 3, 4, 5, 6, 7],
                                                   [2, 4, 6, 8, 10, 12, 14],
                                                   [3, 6, 9, 12, 15, 18, 21],
                                                   [4, 8, 12, 16, 20, 24, 28],
                                                   [5, 10, 15, 20, 25, 30, 35],
                                                   [6, 12, 18, 24, 30, 36, 42],
                                                   [7, 14, 21, 28, 35, 42, 49]]
                         )

    def test_06(self):
        self.assertEqual(multiplication_table(
            3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])

    def test_07(self):
        self.assertEqual(multiplication_table(9), [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                   [2, 4, 6, 8, 10, 12, 14, 16, 18],
                                                   [3, 6, 9, 12, 15,
                                                       18, 21, 24, 27],
                                                   [4, 8, 12, 16, 20,
                                                       24, 28, 32, 36],
                                                   [5, 10, 15, 20, 25,
                                                       30, 35, 40, 45],
                                                   [6, 12, 18, 24, 30,
                                                       36, 42, 48, 54],
                                                   [7, 14, 21, 28, 35,
                                                       42, 49, 56, 63],
                                                   [8, 16, 24, 32, 40,
                                                       48, 56, 64, 72],
                                                   [9, 18, 27, 36, 45, 54, 63, 72, 81]])

    def test_08(self):
        self.assertEqual(multiplication_table(17), [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85], [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102], [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119], [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136], [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153], [
                         10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170], [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187], [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204], [13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195, 208, 221], [14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196, 210, 224, 238], [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255], [16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 272], [17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289]])


if __name__ == '__main__':
    unittest.main(verbosity=2)
