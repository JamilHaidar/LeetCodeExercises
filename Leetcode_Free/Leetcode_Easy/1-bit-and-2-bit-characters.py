# Leetcode 717: 1-bit and 2-bit Characters
# https://leetcode.com/problems/1-bit-and-2-bit-characters

from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0
        while idx<len(bits)-1:
            if bits[idx]==0:
                idx += 1
            else:
                idx += 2
        return idx == len(bits)-1