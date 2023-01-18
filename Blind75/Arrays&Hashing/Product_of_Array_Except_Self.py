# Leetcode 238
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for val in nums[:-1]:
            res.append(res[-1]*val)

        mul=1
        for idx in range(len(nums)-1,-1,-1):
            res[idx] *= mul
            mul*=nums[idx]
        
        return res