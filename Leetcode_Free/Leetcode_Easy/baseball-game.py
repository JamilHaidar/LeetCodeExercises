# Leetcode 682: Baseball Game
# https://leetcode.com/problems/baseball-game

from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for operation in operations:
            if operation == '+':
                score.append(score[-1]+score[-2])
            elif operation == 'D':
                score.append(score[-1]*2)
            elif operation == 'C':
                score.pop()
            else:
                score.append(int(operation))
        return sum(score)