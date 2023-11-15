#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numval1, numval2 = 0, 0

        for i in range(len(num1) - 1, -1, -1):
            numval1 += int(num1[i]) * 10 ** (len(num1) - 1 - i)
            
        for i in range(len(num2) - 1, -1, -1):
            numval2 += int(num2[i]) * 10 ** (len(num2) - 1 - i)
            
        return str(numval1 * numval2)

# @lc code=end

