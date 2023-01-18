# Leetcode 347
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for elem in nums:
            if elem in freq:
                freq[elem] +=1
            else:
                freq[elem] = 1
        freq_sorted = sorted(freq.keys(),key=lambda x:freq[x],reverse=True)
        return freq_sorted[:k]