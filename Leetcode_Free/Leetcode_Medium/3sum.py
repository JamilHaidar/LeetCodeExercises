# Leetcode 15: 3Sum
# https://leetcode.com/problems/3sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        for i in range(len(nums)-2):
            k,j = i+1,len(nums)-1
            while k<j:
                # if (i,j,k) in res:continue
                total = nums[i]+nums[j]+nums[k]
                if total==0:
                    res.add((nums[i],nums[j],nums[k]))
                    k+=1
                    j-=1
                elif total<0:
                    k+=1
                else:
                    j-=1
        return [list(elem) for elem in res]