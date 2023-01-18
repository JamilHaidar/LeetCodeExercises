# Leetcode 121
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for sell in prices[1:]:
            profit = sell-buy
            if profit<0:
                buy=sell
            elif max_profit<sell-buy:
                max_profit = sell-buy
        return max_profit