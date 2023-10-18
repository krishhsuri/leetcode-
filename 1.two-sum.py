#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # A dictionary to store the values and their indices

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], i]

            num_to_index[num] = i

        return []
        
# @lc code=end