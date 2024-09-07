# Leetcode 2129: Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join([elem.title() if len(elem)>2 else elem.lower() for elem in title.split()])