# Leetcode 15
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negative = []
        positive = []
        zero = []
        res = set()
        for elem in nums:
            if elem==0:
                zero.append(elem)
            elif elem>0:
                positive.append(elem)
            else:
                negative.append(elem)
        negSet = set(negative)
        posSet = set(positive)
        if len(zero)>0:
            for elem in negSet:
                if -elem in posSet:
                    res.add((elem,0,-elem))
        if len(zero)>=3:
            res.add((0,0,0))
        for i in range(len(negative)):
            for j in range(i+1,len(negative)):
                if -(negative[i]+negative[j]) in posSet:
                    res.add(tuple(sorted([negative[i],negative[j],-(negative[i]+negative[j])])))
        for i in range(len(positive)):
            for j in range(i+1,len(positive)):
                if -(positive[i]+positive[j]) in negSet:
                    res.add(tuple(sorted([positive[i],positive[j],-(positive[i]+positive[j])])))
        return [list(elem) for elem in res]