# Leetcode 1
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        second = dict()
        for index in range(len(nums)):
            if nums[index] in second:
                return [second[nums[index]],index]
            else:
                second[target - nums[index]] = index
