# Leetcode 213

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def line_rob(nums):
            rob1 , rob2 = 0,0 
            for val in nums:
                temp = max(val+rob1,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(nums[0],line_rob(nums[1:]),line_rob(nums[:-1]))

nums = [2,3,2]
# nums = [1,2,3,1]
sol = Solution()
print(sol.rob(nums))