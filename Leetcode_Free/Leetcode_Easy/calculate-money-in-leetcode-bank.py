# Leetcode 1716: Calculate Money in Leetcode Bank
# https://leetcode.com/problems/calculate-money-in-leetcode-bank

class Solution:
    def totalMoney(self, n: int) -> int:
        return 28 * (n//7) + 7*sum(range(n//7)) + (n%7) * (n//7)+sum(range(1+n%7))