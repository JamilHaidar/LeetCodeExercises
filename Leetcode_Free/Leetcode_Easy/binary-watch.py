# Leetcode 401: Binary Watch
# https://leetcode.com/problems/binary-watch

from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for hour in range(12):
            for minute in range(60):
                if (bin(hour)+bin(minute)).count('1') == turnedOn:
                    ans.append(f'{hour}:{minute:02}')
        return ans