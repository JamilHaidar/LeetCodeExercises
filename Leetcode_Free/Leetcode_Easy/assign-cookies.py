# Leetcode 455: Assign Cookies
# https://leetcode.com/problems/assign-cookies
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        child_pointer = 0
        for cookie_size in s:
            if g[child_pointer] <= cookie_size: # least greedy child can be satisfied
                child_pointer += 1
            if child_pointer==len(g):break
        return child_pointer