# Leetcode 1502: Can Make Arithmetic Progression From Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        dt = arr[1]-arr[0]
        for idx in range(1,len(arr)):
            if arr[idx]-arr[idx-1] !=dt:
                return False
        return True