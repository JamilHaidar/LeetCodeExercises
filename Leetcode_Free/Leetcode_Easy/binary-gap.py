# Leetcode 868: Binary Gap
# https://leetcode.com/problems/binary-gap
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        current_count = 0
        started = False
        while n:
            bit = n&1
            if bit:
                if started:
                    ans = max(ans,current_count+1)
                else:
                    started = True
            elif started:
                current_count+=1
            n = n>>1
        return ans