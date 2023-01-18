# Leetcode 424
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frequency = defaultdict(int)
        left = 0
        max_length = 0
        max_frequency = 0

        for right,elem in enumerate(s):
            frequency[elem]+=1
            max_frequency = max(max_frequency,frequency[elem])
            while (right-left+1) - max_frequency>k:
                frequency[s[left]]-=1
                left+=1                
            max_length = max(max_length,right-left+1)
        return max_length