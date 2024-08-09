# Leetcode 704: Binary Search
# https://leetcode.com/problems/binary-search
from typing import List
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Manual method
        # l = 0
        # r = len(nums)-1
        # while l<=r:
        #     mid = (l+r)//2
        #     if mid<target:
        #         l = mid + 1
        #     elif mid>target:
        #         r = mid - 1
        #     else:
        #         return mid
        # return -1

        # Built in method
        index = bisect.bisect_left(nums,target)
        if index !=len(nums) and nums[index]==target:
            return index
        return -1
    