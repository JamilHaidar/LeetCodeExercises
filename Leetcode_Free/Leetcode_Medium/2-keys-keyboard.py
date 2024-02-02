# Leetcode 650: 2 Keys Keyboard
# https://leetcode.com/problems/2-keys-keyboard
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for elem in range(n+1)]
        for target_length in range(2,n+1):
            dp[target_length] = target_length
            for possible_divisor in range(target_length-1,1,-1):
                if target_length%possible_divisor == 0:
                    dp[target_length] = dp[possible_divisor]+target_length//possible_divisor
                    break
        return dp[-1]

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        res = 0
        divider = 2
        while divider < n:
            if n % divider == 0:
                res += divider
                n = n // divider
                continue
            divider += 1
        return res+n
    
sol = Solution()
print(sol.minSteps(9))
    