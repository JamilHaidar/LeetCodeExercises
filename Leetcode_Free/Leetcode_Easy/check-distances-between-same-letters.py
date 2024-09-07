# Leetcode 2399: Check Distances Between Same Letters
# https://leetcode.com/problems/check-distances-between-same-letters

from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = dict()
        for index in range(len(s)):
            if s[index] in seen:
                if distance[ord(s[index])-ord('a')]!= (index - seen[s[index]]-1):
                    return False
            else:
                seen[s[index]] = index
        return True