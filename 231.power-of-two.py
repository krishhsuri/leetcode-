#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=1
        if n ==1 :
            return True
        while i<n:
            i *=2 
            if i ==n :
                return True
        return False
        
# @lc code=end

