# Leetcode 561: Array Partition
# https://leetcode.com/problems/array-partition
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        for i in range(len(nums)//2):
            ans += nums[i*2]
        return ans