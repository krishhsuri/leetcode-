#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = [0] * (len(nums) + 1)
        for i in nums:
            cnt[i] += 1
            if cnt[i] > 1:
                return i
        return len(nums)
        
# @lc code=end

