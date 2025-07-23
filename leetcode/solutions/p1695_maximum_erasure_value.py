# solutions/p1695_maximum_erasure_value.py

from typing import List

class Solution:
    def maximumErasureValue(self, nums: List[int]) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        for i, x in enumerate(nums):
            P[i+1] = P[i] + x

        MAXV = 10000
        last = [-1] * (MAXV + 1)
        ans = 0
        left = 0

        for i, x in enumerate(nums):
            j = last[x]
            if j >= left:
                left = j + 1

            curr = P[i+1] - P[left]
            if curr > ans:
                ans = curr

            last[x] = i

        return ans


if __name__ == "__main__":

    # Basic Test
    nums = [4, 2, 4, 5, 6]
    result = Solution().maximumErasureValue(nums)
    print("Result:", result)
