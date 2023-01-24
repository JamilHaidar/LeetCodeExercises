# Leetcode 98
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if (node.val >= right) or (node.val <= left):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))