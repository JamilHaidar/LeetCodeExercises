# Leetcode 2119: A Number After a Double Reversal
# https://leetcode.com/problems/a-number-after-a-double-reversal

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp = num
        reversed1 = 0
        while temp:
            reversed1 = reversed1*10 + temp%10
            temp = temp // 10
        temp = reversed1
        reversed2 = 0
        while temp:
            reversed2 = reversed2*10 + temp%10
            temp = temp // 10
        return reversed2==num