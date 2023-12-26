#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=[1]*len(nums)
        pre = 1 
        post =1 
        for i in range(len(nums)):
            x[i] = pre
            pre *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            x[i] *= post
            post *= nums[i]
        return x
        
# @lc code=end

