#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(0,len(nums2)):
            nums1[m+i] = nums2[i]
        for i in range(1,len(nums1)):
            x = nums1[i]
            j = i-1
            while j >=0 and x < nums1[j]:
                nums1[j+1] = nums1[j]
                j-=1
            nums1[j+1] = x
        return nums1
        
# @lc code=end

