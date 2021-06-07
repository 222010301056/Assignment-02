# pylint: disable=invalid-name
"""
Stairway To Heaven
Given a list of integers nums, for each element,
add its index to its value and return the new list.

For example, given the list [5, 3, 7], return [5, 4, 9]
since it's [5 + 0, 3 + 1, 7 + 2].

Example 1
Input
nums = [5, 3, 7]

Output
[5, 4, 9]
"""




# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def stairway_to_heaven(nums):

    for i in range(len(nums)):
        nums[i]=nums[i]+i
    return nums

# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable,line-too-long
class TestStairwayToHeaven(unittest.TestCase):

    def test_01(self):
        self.assertEqual(stairway_to_heaven([5, 3, 7]), [5, 4, 9])

    def test_02(self):
        self.assertEqual(stairway_to_heaven([0, 0, 0]), [0, 1, 2])

    def test_03(self):
        self.assertEqual(stairway_to_heaven([]), [])

    def test_04(self):
        self.assertEqual(stairway_to_heaven([0]), [0])

    def test_05(self):
        self.assertEqual(stairway_to_heaven([0, 1]), [0, 2])

    def test_06(self):
        self.assertEqual(stairway_to_heaven(
            [24, 23, 22, 21]), [24, 24, 24, 24])

    def test_07(self):
        self.assertEqual(stairway_to_heaven(
            [106, 189, 209, 143]), [106, 190, 211, 146])

    def test_08(self):
        self.assertEqual(stairway_to_heaven(
            [419, 249, 255, 308, 243, 343, 451, 451, 393, 275, 169, 227]), [419, 250, 257, 311, 247, 348, 457, 458, 401, 284, 179, 238])


if __name__ == '__main__':
    unittest.main(verbosity=2)
