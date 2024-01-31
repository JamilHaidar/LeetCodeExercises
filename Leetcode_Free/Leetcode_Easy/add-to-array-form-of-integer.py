# Leetcode 989: Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer

from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(map(int,str(int(''.join(map(str,num)))+k)))