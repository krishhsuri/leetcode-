#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1,len(nums)):
            x = nums[i]
            j =i-1
            while j>=0 and nums[j] >x :
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = x         
# @lc code=end

