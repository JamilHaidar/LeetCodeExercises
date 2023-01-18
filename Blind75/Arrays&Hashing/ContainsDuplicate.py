#LeetCode 217
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for elem in nums:
            if elem in seen:
                return True
            seen.add(elem)
        return False