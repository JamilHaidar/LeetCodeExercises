# Leetcode 2455: Average Value of Even Numbers That Are Divisible by Three
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three
from typing import List
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = 0
        total = 0
        for elem in nums:
            if elem%6 == 0:
                ans+=elem
                total += 1
        if total==0:return 0
        return ans//total