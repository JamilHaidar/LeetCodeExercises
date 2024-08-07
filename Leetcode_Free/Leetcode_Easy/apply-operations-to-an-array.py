# Leetcode 2460: Apply Operations to an Array
# https://leetcode.com/problems/apply-operations-to-an-array
from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                i+=1
            i+=1
        res = []
        for num in nums:
            if num>0:
                res.append(num)
        return res + [0]*(len(nums)-len(res))