# Leetcode 605: Can Place Flowers
# https://leetcode.com/problems/can-place-flowers

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # for index in range(len(flowerbed)):
        #     if flowerbed[index]==0:
        #         if 0<index<len(flowerbed)-1:
        #             if flowerbed[index-1]==0 and flowerbed[index+1]==0:
        #                 n-=1
        #                 flowerbed[index] = 1
        #         elif (index == 0 and flowerbed[index+1]==0) or (index == len(flowerbed)-1 and flowerbed[index-1]==0):
        #             n-=1
        #             flowerbed[index] = 1
        #     if n==0:return True
        # return False
        flowerbed = [0] + flowerbed + [0]
        for index in range(1,len(flowerbed)-1):
            if flowerbed[index-1]==0 and flowerbed[index]==0 and flowerbed[index+1]==0:
                flowerbed[index] = 1
                n-=1
        return n<=0