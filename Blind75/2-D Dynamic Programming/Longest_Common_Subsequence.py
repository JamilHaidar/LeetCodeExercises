# Leetcode 1143

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for t2_idx in range(1,len(text2)+1):
            for t1_idx in range(1,len(text1)+1):
                if text2[t2_idx-1]==text1[t1_idx-1]:
                    dp[t2_idx][t1_idx] = 1 + dp[t2_idx-1][t1_idx-1]
                else:
                    dp[t2_idx][t1_idx] = max(dp[t2_idx][t1_idx-1],dp[t2_idx-1][t1_idx])
        # for row in dp:
        #     print(row)
        return dp[-1][-1]

text1 = "abcde"
text2 = "ace"

sol = Solution()
print(sol.longestCommonSubsequence(text1,text2))