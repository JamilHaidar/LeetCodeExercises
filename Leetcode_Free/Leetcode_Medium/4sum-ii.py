# Leetcode 454: 4Sum II
# https://leetcode.com/problems/4sum-ii

from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mapping = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                mapping[num1+num2] += 1
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                count += mapping[-(num3+num4)]
        return count