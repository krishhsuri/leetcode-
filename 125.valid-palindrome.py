#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        x=""
        for i in s :
             if 'a' <= i <= 'z' or "0"<= i <= "9":
                x += i
        return x == x[::-1]
        
# @lc code=end

