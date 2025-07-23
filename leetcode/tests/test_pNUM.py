# tests/test_p1696.py

import unittest
from leetcode.solutions.pNUM_DESCRIPTION import Solution

class TestProblemDescription(unittest.TestCase):
    def run_test(self, nums, expected):
        sol = Solution()
        self.assertEqual(sol.problemDescription(nums), expected)

    def test_examples(self):
        # LeetCode examples
        self.run_test([4,2,4,5,6], None)
        self.run_test([5,2,1,2,5,2,1,2,5], None)

    def test_edge_cases(self):
        # Your own boundary / random tests
        self.run_test([], None)
        self.run_test([100], None)
        self.run_test([1,1,1,1], None)

    # Add more as you like…

if __name__ == "__main__":
    unittest.main()
