# Leetcode 647

class Solution:
    def countSubstrings(self, s: str) -> int:
        substring_sum = 0
        for index in range(len(s)):
            left, right = index, index
            while left>-1 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                substring_sum+=1
                
            left, right = index, index+1
            while left>-1 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                substring_sum+=1
        return substring_sum

s = "aaa"
# s = "abc"
sol = Solution()
print(sol.countSubstrings(s))