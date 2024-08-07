# Leetcode 2544: Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        mul = 1
        while n>0:
            ans += mul*(n%10)
            n = n//10
            mul *= -1
        if mul==-1:return -ans
        return ans