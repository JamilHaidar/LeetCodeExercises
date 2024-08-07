# Leetcode 18: 4Sum
# https://leetcode.com/problems/4sum

from typing import List

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = set()
#         nums = sorted(nums)
#         for i in range(len(nums)-3):
#             for m in range(i+1,len(nums)-2):
#                 k,j = m+1,len(nums)-1
#                 while k<j:
#                     total = nums[i]+nums[m]+nums[j]+nums[k]
#                     if total==target:
#                         res.add((nums[i],nums[m],nums[j],nums[k]))
#                         k+=1
#                         j-=1
#                     elif total<target:
#                         k+=1
#                     else:
#                         j-=1
#         return [list(elem) for elem in res]
    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def ksum(nums, target, k):
            res = []
            if not nums: return res

            avg = target // k
            if avg < nums[0] or nums[-1] < avg: return res
            if k == 2: return twosum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in ksum(nums[i+1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res

        def twosum(nums, target):
            res = []
            visited = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in visited:
                        res.append([target-nums[i], nums[i]])
                visited.add(nums[i])
            return res
        nums.sort()
        return ksum(nums, target, 4)