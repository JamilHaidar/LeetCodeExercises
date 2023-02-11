# Leetcode 417

from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        m = len(heights)
        n = len(heights[0])
        def search(row,col,ocean,prevHeight):
            within_borders = row>-1 and row<m and col>-1 and col<n
            if not within_borders:return
            if heights[row][col]<prevHeight:return
            if (row,col) in ocean:return
            ocean.add((row,col))
            search(row+1,col,ocean,heights[row][col])
            search(row-1,col,ocean,heights[row][col])
            search(row,col+1,ocean,heights[row][col])
            search(row,col-1,ocean,heights[row][col])
        for row_idx in range(m):
            search(row_idx,0,pacific,heights[row_idx][0])
            search(row_idx,n-1,atlantic,heights[row_idx][n-1])
        for col_idx in range(n):
            search(0,col_idx,pacific,heights[0][col_idx])
            search(m-1,col_idx,atlantic,heights[m-1][col_idx])
 
        found = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    found.append([i,j])
        return found

# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
heights = [[1,1],[1,1],[1,1]]

sol = Solution()
print(sol.pacificAtlantic(heights))