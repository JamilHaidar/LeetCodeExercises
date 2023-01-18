# Leetcode 76
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        remaining_count = len(t)
        found_left, found_right = 0,len(s)+1
        characters_needed = defaultdict(int)

        for elem in t:
            characters_needed[elem] += 1
        left = 0
        for right,elem in enumerate(s):
            if characters_needed[elem]>0:
                remaining_count-=1
            characters_needed[elem] -= 1
            if remaining_count==0:
                while characters_needed[s[left]]<0:
                    characters_needed[s[left]]+=1
                    left += 1
                if right-left+1 <found_right-found_left+1:
                    found_right,found_left = right+1, left
                
                characters_needed[s[left]]+=1
                left+=1
                remaining_count+=1
        return s[found_left:found_right] if found_right!=len(s)+1 else ''