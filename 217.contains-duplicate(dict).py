#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen= {}
        for num in nums :
            if num in seen and seen[num] >= 1 :
                return True
            seen[num] = seen.get(num,0) + 1
# @lc code=end

