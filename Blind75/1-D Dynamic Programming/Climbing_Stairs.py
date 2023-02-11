# Leetcode 70
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2: return 2
        prev = 2
        prevprev = 1
        current = prev
        for _ in range(3,n+1):
            current = prev+prevprev
            prevprev = prev
            prev = current
        return current

sol = Solution()
print(sol.climbStairs(4))