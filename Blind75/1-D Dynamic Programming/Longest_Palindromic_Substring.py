# Leetcode 5

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        max_length = 0
        for index in range(len(s)):
            left, right = index, index
            while left>-1 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            if right-left-1>max_length:
                max_length = right-left-1
                res = s[left+1:right]
                
            left, right = index, index+1
            while left>-1 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            if right-left-1>max_length:
                max_length = right-left-1
                res = s[left+1:right]
        return res

# s = "babad"
s = "bb"
sol = Solution()
print(sol.longestPalindrome(s))