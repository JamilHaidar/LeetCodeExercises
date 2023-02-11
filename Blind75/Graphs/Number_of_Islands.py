# Leetcode 200

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        def search(row,col):
            within_borders = row>-1 and row<m and col>-1 and col<n
            if not within_borders:return 
            if (row,col) in visited: return
            if grid[row][col] == '0': return
            visited.add((row,col))
            search(row+1,col)
            search(row-1,col)
            search(row,col+1)
            search(row,col-1)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    res+=1
                    search(i,j)
        return res

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
print(sol.numIslands(grid))