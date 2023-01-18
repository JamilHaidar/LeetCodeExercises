# Leetcode 11
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left<right:
            current_area = (right-left)*min(height[right],height[left])
            if current_area>max_area:
                max_area = current_area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area