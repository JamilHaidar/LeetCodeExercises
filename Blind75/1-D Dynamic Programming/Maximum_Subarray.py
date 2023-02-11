# Leetcode 53

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_of_prev = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            max_of_prev = max(max_of_prev+nums[i],nums[i])
            result = max(result,max_of_prev)
        return result

        # Slightly more efficient:
        # current_sum = 0
        # max_sum = nums[0]
        # for index in range(len(nums)):
        #     current_sum = current_sum + nums[index]
        #     if max_sum<current_sum:
        #         max_sum = current_sum
        #     if current_sum<0:
        #         current_sum = 0
        # return max_sum

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))