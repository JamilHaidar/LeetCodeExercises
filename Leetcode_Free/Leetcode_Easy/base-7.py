# Leetcode 504: Base 7
# https://leetcode.com/problems/base-7

class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ''
        sign = ''
        if num<0:
            sign = '-'
            num *= -1
        elif num==0:
            return '0'
        while num:
            ans = str(num%7) + ans
            num = num//7
        return sign+ans