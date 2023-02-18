# Leetcode 322

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount==0:return 0
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for target in range(1,amount+1):
            for coin in coins:
                if target-coin>=0:
                    dp[target] = min(dp[target],1+dp[target-coin])
                
        return dp[amount] if dp[amount]!=amount+1 else -1 
coins = [1,2,5]
amount = 11

coins = [2]
amount = 3
coins = [1]
amount = 0
# coins = [2147483647]
# amount = 2
sol = Solution()
print(sol.coinChange(coins,amount))