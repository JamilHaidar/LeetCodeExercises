# Leetcode 2706: Buy Two Chocolates
# https://leetcode.com/problems/buy-two-chocolates

from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        return money if money<(prices[0]+prices[1]) else money-prices[0]-prices[1]