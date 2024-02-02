# Leetcode 542: 01 Matrix
# https://leetcode.com/problems/01-matrix

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = []
        seeds = deque()
        for row_index in range(len(mat)):
            dist.append([])
            for col_index in range(len(mat[row_index])):
                if mat[row_index][col_index]==0:
                    seeds.append((row_index,col_index))
                    dist[row_index].append(0)
                else:
                    dist[row_index].append(-1)
        dirs = [[-1,0],[0,-1],[0,1],[1,0]]
        while seeds:
            row_index,col_index = seeds.popleft()
            for direction in dirs:
                if 0<=row_index+direction[0]<len(mat) and 0<=col_index+direction[1]<len(mat[row_index]) and dist[row_index+direction[0]][col_index+direction[1]]==-1:
                    dist[row_index+direction[0]][col_index+direction[1]] = 1+dist[row_index][col_index]
                    seeds.append((row_index+direction[0],col_index+direction[1]))
        return dist
