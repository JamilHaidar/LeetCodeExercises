# Leetcode 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left_pointer = 0
        mapping = dict()
        for i,elem in enumerate(s):
            if elem in mapping and mapping[elem]>=left_pointer:
                left_pointer = mapping[elem]+1
            elif max_length<i-left_pointer+1:
                max_length = i-left_pointer+1
            mapping[elem] = i
        return max_length