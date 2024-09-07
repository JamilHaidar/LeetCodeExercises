# Leetcode 2525: Categorize Box According to Criteria
# https://leetcode.com/problems/categorize-box-according-to-criteria
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = length>=10000 or width >= 10000 or height >=10000 or (length*width*height) >= 1e9
        heavy = mass>=100
        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        return "Neither"