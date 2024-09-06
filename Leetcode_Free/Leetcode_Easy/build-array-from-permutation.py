# Leetcode 1920: Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for index in range(len(nums)):
            ans.append(nums[nums[index]])
        return ans