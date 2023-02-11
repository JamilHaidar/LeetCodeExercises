# Leetcode 79

from typing import List
from collections import defaultdict,Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        m = len(board)
        n = len(board[0])
        visited = set()
        def search(row_idx:int,col_idx:int,curr_word_len):
            within_borders = row_idx>-1 and row_idx<m and col_idx>-1 and col_idx<n
            if not within_borders: return False
            if board[row_idx][col_idx] != word[curr_word_len]: return False
            if (row_idx,col_idx) in visited: return False
            visited.add((row_idx,col_idx))
            curr_word_len += 1
            if curr_word_len == len(word):return True
            if search(row_idx+1,col_idx,curr_word_len): return True
            if search(row_idx-1,col_idx,curr_word_len): return True
            if search(row_idx,col_idx+1,curr_word_len): return True
            if search(row_idx,col_idx-1,curr_word_len): return True
            visited.remove((row_idx,col_idx))
            curr_word_len -= 1
            return False
        for row in range(m):
            for col in range(n):
                if search(row,col,0):
                    return True
        return False

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]]

word = "CCC"
sol = Solution()
print(sol.exist(board,word))