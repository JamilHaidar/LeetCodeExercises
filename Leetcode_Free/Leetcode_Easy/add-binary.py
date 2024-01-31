# Leetcode 67: Add Binary
# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''
        idx_a = len(a)-1
        idx_b = len(b)-1
        while idx_a>-1 or idx_b>-1:
            if idx_a>-1:
                carry += int(a[idx_a])
                idx_a -= 1
            if idx_b>-1:
                carry += int(b[idx_b])
                idx_b -= 1
            res = str(carry%2) + res
            carry = carry // 2
            
        if carry:res = '1' + res
        return res