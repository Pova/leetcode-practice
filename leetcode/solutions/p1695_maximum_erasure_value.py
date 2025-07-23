# solutions/p1695_maximum_erasure_value.py

from typing import List

class Solution:
    def maximumErasureValue(self, nums: List[int]) -> int:
        
        """
        Solution might work but be too inefficient.
        """
        
        # [v, -, -, v, -]
        # [a, b, c, d, e]

        array_len = len(nums)
        left_idx = 0
        best_so_far = nums[0]
        int_set = set([nums[0]])
        current_sum = nums[0]

        # move the right idx

        for right_idx in range(left_idx+1, array_len):
            
            new_num = nums[right_idx]

            # check if new number is a duplicate

            if new_num in int_set:
                # encountered a duplicate
                # need to move the left index to the right until we encounter the same number
                
                # encountered a duplicate
                # [v, -, -, -, -, v]
                # [1, 2, 3, 4, 5, 3]
                # left = 1
                # int_set = {1, 2, 3, 4, 5}
                
                # [-, v, -, -, -, v]
                # [1, 2, 3, 4, 5, 3]
                # left = 2
                # int_set = {2, 3, 4, 5}
                
                # [-, -, v, -, -, v]
                # [1, 2, 3, 4, 5, 3]
                # left = 3
                # int_set = {3, 4, 5}
                
                # [1, 2, 3, 4, 5]
                while nums[left_idx] != new_num:
                    int_set.remove(nums[left_idx])
                    current_sum -= nums[left_idx]
                    left_idx += 1
                
                # current sum stays the same
                left_idx += 1
                
            else:
                # not a duplicate
                
                # add to int set
                # add to current sum
                
                int_set.add(new_num)
                current_sum += new_num
                
                if current_sum > best_so_far:
                    best_so_far = current_sum

        return best_so_far


if __name__ == "__main__":

    # Basic Test
    nums = [4, 2, 4, 5, 6]
    result = Solution().maximumErasureValue(nums)
    print("Result:", result)
