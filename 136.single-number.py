#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List
class Solution:
    def singleNumber(self, x: List[int]) -> int:
        y ={}
        for i in x :
            if i in y:
                y[i] +=1
            else :
                y[i] =1 
        for k,v in y.items():
            if v ==1:
                return k

        
# @lc code=end

