#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0 
        min_buy = prices[0]
        for i in range(len(prices)):
            profit = max(prices[i]-min_buy,profit)
            min_buy = min(min_buy,prices[i])
        return profit

        
# @lc code=end

