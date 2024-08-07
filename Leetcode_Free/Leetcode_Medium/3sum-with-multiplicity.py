# Leetcode 923: 3Sum With Multiplicity
# https://leetcode.com/problems/3sum-with-multiplicity

from typing import List
from collections import Counter
import math

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counts = Counter(arr)
        sorted_arr = sorted(set(arr))
        res = 0
        for i,elem in enumerate(sorted_arr):
            k, j = i + 1, len(sorted_arr) - 1
            if counts[elem]>1 and target-elem*2 in counts:
                if elem*3==target:
                    res += math.comb(counts[elem],3)
                else:
                    res += (counts[elem]*(counts[elem]-1))//2 * counts[target-elem*2]
            while k<j:
                num2 , num3 = sorted_arr[k],sorted_arr[j]
                total = elem + num2 + num3
                if total==target:
                    res += counts[elem]*counts[num2]*counts[num3]
                    k+=1
                    j-=1
                elif total<target:
                    k+=1
                else:
                    j-=1
        return res % (10**9+7)