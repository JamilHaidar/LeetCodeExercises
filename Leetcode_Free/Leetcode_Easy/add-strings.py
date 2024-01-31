# Leetcode 415: Add Strings
# https://leetcode.com/problems/add-strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = ''
        idx_num1 = len(num1)-1
        idx_num2 = len(num2)-1
        while idx_num1>-1 or idx_num2>-1:
            if idx_num1>-1:
                carry += int(num1[idx_num1])
                idx_num1 -= 1
            if idx_num2>-1:
                carry += int(num2[idx_num2])
                idx_num2 -= 1
            res = str(carry%10) + res
            carry = carry // 10
            
        if carry:res = str(carry) + res
        return res