# Leetcode 49
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for word in strs:
            base = ''.join(sorted(word))
            if base in anagrams:
                anagrams[base].append(word)
            else:
                anagrams[base] = [word]
        return anagrams.values()