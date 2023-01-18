# Leetcode 128
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for elem in nums:
            if (elem-1) not in nums:
                length=1
                while elem+length in nums:
                    length+=1
                max_length = max(length,max_length)
        return max_length