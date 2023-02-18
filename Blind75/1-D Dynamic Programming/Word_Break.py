# Leetcode 139

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for char_idx in range(len(s)-1,-1,-1):
            for word in wordDict:
                if char_idx+len(word)<=len(s) and s[char_idx:char_idx+len(word)]==word:
                    dp[char_idx] = dp[char_idx + len(word)]
                if dp[char_idx]:break
        return dp[0]
s = "leetcode"
wordDict = ["leet","code"]

sol = Solution()
print(sol.wordBreak(s,wordDict))