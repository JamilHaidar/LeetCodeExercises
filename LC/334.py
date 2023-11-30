from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = float('inf')
        mid = float('inf')
        for right in nums:
            if right<=left:
                left = right
            elif right<=mid:
                mid = right
            else:
                return True
        return False

nums = [2,1,5,0,4,6]
sol = Solution()
print(sol.increasingTriplet(nums))