# Leetcode 91

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':return 0
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and int(s[i:i+2])<27:
                dp[i] += dp[i + 2]
        return dp[0]
s = "12"
# s = "06"
# s = "10"
# s = "27"
# s = "226"
s = "1123"
sol = Solution()
print(sol.numDecodings(s))
# 1
# 1 1, 11
# 1 1 2, 11 2, 1 12
#