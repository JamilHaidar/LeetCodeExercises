# Leetcode 198

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 , rob2 = 0,0 
        for val in nums:
            temp = max(val+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

nums = [2,1,1,2]
# nums = [2,7,9,3,1,2]
sol = Solution()
print(sol.rob(nums))