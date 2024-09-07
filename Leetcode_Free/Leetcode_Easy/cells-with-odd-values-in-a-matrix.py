# Leetcode 1252: Cells with Odd Values in a Matrix
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix

from typing import List
from collections import defaultdict
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        for index in indices:
            rows[index[0]] += 1
            cols[index[1]] += 1

        c_odd_count = sum([1 for c in cols.values() if c&1])
        r_odd_count = sum([1 for r in rows.values() if r&1])
        total_odds = m*c_odd_count + n*r_odd_count - 2*c_odd_count*r_odd_count
        return total_odds