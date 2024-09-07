# Leetcode 1640: Check Array Formation Through Concatenation
# https://leetcode.com/problems/check-array-formation-through-concatenation

from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piece_mapping = {elem[0]:elem for elem in pieces}
        res = []
        for elem in arr:
            res += piece_mapping.get(elem,[])
        return res == arr