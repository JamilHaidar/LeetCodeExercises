# Leetcode 2828: Check if a String Is an Acronym of Words
# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words

from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return ''.join([elem[0] for elem in words])==s