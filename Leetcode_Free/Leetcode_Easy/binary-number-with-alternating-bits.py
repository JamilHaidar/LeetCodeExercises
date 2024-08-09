# Leetcode 693: Binary Number with Alternating Bits
# https://leetcode.com/problems/binary-number-with-alternating-bits
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = -1
        while n:
            current_bit = n&1
            if prev_bit == current_bit:return False
            prev_bit = current_bit
            n = n>>1
        return True