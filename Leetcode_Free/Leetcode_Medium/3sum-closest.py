# Leetcode 16: 3Sum Closest
# https://leetcode.com/problems/3sum-closest

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = 100000
        nums = sorted(nums)
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                current_sum = nums[i]+nums[j]+nums[k]
                if current_sum==target:return target
                if current_sum>target:
                    k -=1
                else:
                    j += 1
                if abs(target-closest_sum) > abs(target-current_sum):
                    closest_sum = current_sum
        return closest_sum    
