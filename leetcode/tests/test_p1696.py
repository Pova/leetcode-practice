# tests/test_p1696.py

import unittest
from leetcode.solutions.p1696_maximum_unique_subarray import Solution

class TestMaximumUniqueSubarray(unittest.TestCase):
    def run_test(self, nums, expected):
        sol = Solution()
        self.assertEqual(sol.maximumUniqueSubarray(nums), expected)

    def test_examples(self):
        # LeetCode examples
        self.run_test([4,2,4,5,6], 17)
        self.run_test([5,2,1,2,5,2,1,2,5], 8)

    def test_edge_cases(self):
        # Your own boundary / random tests
        self.run_test([], 0)
        self.run_test([100], 100)
        self.run_test([1,1,1,1], 1)

    # Add more as you like…

if __name__ == "__main__":
    unittest.main()
