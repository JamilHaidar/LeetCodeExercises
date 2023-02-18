# Leetcode 300

from typing import List

class Solution:
    def lengthOfLIS2(self, nums: List[int]) -> int:
        # O(n^2)
        dp = [1]*len(nums)
        for curr_idx in range(len(nums)-2,-1,-1):
            for prev_idx in range(curr_idx+1,len(nums)):
                if nums[curr_idx]<nums[prev_idx]:
                    dp[curr_idx] = max(dp[curr_idx],1+dp[prev_idx])
        return max(dp)
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        # O(nlogn)
        subsequence = []
        for number in nums:
            # if subsequence is empty, add number
            # if last element in subsequence less than number, add it
            if len(subsequence) == 0 or subsequence[-1] < number:
                subsequence.append(number)
            else:
                # if last element in subsequence is less than the number, keep same size but insert it in
                idx = bisect_left(subsequence, number)
                subsequence[idx] = number

        return len(subsequence)

    def pathOfLIS(self, nums: List[int]):
        from bisect import bisect_left
        sub = []
        subIndex = []  # Store index instead of value for tracing path purpose
        trace = [-1] * len(nums)  # trace[i] point to the index of previous number in LIS
        for i, x in enumerate(nums):
            if len(sub) == 0 or sub[-1] < x:
                if subIndex:
                    trace[i] = subIndex[-1]
                sub.append(x)
                subIndex.append(i)
            else:
                idx = bisect_left(sub, x)  # Find the index of the smallest number >= x, replace that number with x
                if idx > 0:
                    trace[i] = subIndex[idx - 1]
                sub[idx] = x
                subIndex[idx] = i

        path = []
        t = subIndex[-1]
        while t >= 0:
            path.append(nums[t])
            t = trace[t]
        return path[::-1]

nums = [10,9,2,5,3,7,101,18]
sol = Solution()
print(sol.lengthOfLIS(nums))