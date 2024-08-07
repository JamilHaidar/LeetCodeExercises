# Leetcode 441: Arranging Coins
# https://leetcode.com/problems/arranging-coins
# from math import floor,sqrt

class Solution:
    def arrangeCoins(self, n: int) -> int:

        # Binary search with depending on last move being right = right-1
        # l = 1
        # r = n
        # while l<=r:
        #     mid = (l+r)//2
        #     coin_count = mid*(mid+1)/2
        #     if coin_count <= n:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return r
    
        # Binary search without the assumption
        l = 1
        r = n
        res = 0
        while l<=r:
            mid = (l+r)//2
            coin_count = mid*(mid+1)/2
            if coin_count <= n:
                l = mid + 1
                res = max(res,mid)
            else:
                r = mid - 1
        return res
    
        # return floor((-1+sqrt(1+8*n))/2)