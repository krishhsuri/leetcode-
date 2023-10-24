#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for i in strs :
            sort_strs = "".join(sorted(i))
            if sort_strs not in x :
                x[sort_strs] = [i]
            else:
                x[sort_strs].append(i)
        y =[]
        for value in x.values():
            y.append(value)
        return y

# @lc code=end

