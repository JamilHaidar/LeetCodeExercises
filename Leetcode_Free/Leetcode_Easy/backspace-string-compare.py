# Leetcode 844: Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_typed = ''
        for elem in s:
            if elem=='#':
                s_typed = s_typed[:-1]
            else:
                s_typed = s_typed + elem
        t_typed = ''
        for elem in t:
            if elem=='#':
                t_typed = t_typed[:-1]
            else:
                t_typed = t_typed + elem
        return s_typed == t_typed 