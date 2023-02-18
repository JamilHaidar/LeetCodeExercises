# Leetcode 152

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_product = 1
        min_product = 1
        for element in nums:
            temp_max_product = element*max_product
            max_product = max(temp_max_product,element*min_product,element)
            min_product = min(temp_max_product,element*min_product,element)
            res = max(res,max_product)
        return res
                

nums = [2,3,-2,4]

sol = Solution()
print(sol.maxProduct(nums))