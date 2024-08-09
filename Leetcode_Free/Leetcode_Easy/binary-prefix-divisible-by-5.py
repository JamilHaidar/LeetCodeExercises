# Leetcode 1018: Binary Prefix Divisible By 5
# https://leetcode.com/problems/binary-prefix-divisible-by-5
from typing import List
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        current_remainder = 0
        ans = []
        for num in nums:
            current_remainder = (2*current_remainder+num)%5
            ans.append(current_remainder==0)
        return ans