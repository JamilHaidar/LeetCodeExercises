# Leetcode 2243: Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            s = ''.join([str(sum(map(int,list(s[i:i+k])))) for i in range(0,len(s),k)])
        return s