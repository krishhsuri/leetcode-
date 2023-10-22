#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x={}
        y=[]
        for i in nums:
            if i in x  :
                x[i]  +=1
            else :
                x[i] =1 
        for j in range(k):
            max_val =0
            max_key =0
            for key,val in x.items():
                if val > max_val:
                    max_val = val 
                    max_key = key
            y.append(max_key)
            x.pop(max_key)
        return y

# @lc code=end

