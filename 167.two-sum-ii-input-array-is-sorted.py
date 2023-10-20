#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = {}
        for i,j in enumerate(numbers):
            y = target-j
            if y in x:
                return[x[y]+1,i+1]
            x[j] =i
        return []

# @lc code=end

