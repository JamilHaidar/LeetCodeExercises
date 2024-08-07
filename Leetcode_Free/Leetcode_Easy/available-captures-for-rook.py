# Leetcode 999: Available Captures for Rook
# https://leetcode.com/problems/available-captures-for-rook
from typing import List
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_r,rook_c = 0,0
        for row in range(8):
            found = False
            for column in range(8):
                if board[row][column] == 'R':
                    rook_r,rook_c = row,column
                    break
            if found:break
        # check right
        ans = 0
        for potential_square in range(rook_c+1,8):
            if board[rook_r][potential_square]=='B':
                break
            elif board[rook_r][potential_square]=='p':
                ans+=1
                break

        # check left
        for potential_square in range(rook_c-1,-1,-1):
            if board[rook_r][potential_square]=='B':
                break
            elif board[rook_r][potential_square]=='p':
                ans+=1
                break

        # check down
        for potential_square in range(rook_r+1,8):
            if board[potential_square][rook_c]=='B':
                break
            elif board[potential_square][rook_c]=='p':
                ans+=1
                break
        
        # check up
        for potential_square in range(rook_r-1,-1,-1):
            if board[potential_square][rook_c]=='B':
                break
            elif board[potential_square][rook_c]=='p':
                ans+=1
                break

        return ans