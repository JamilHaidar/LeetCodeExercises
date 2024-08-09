# Leetcode 121: Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for current_price in prices[1:]:
            if current_price<buy:
                buy = current_price
            else:
                profit = max(profit,current_price-buy)
        return profit