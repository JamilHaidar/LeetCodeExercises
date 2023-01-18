# Leetcode 125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''
        for elem in s:
            if elem.isalnum():
                cleaned_str+=elem.lower()
        return cleaned_str==cleaned_str[::-1]