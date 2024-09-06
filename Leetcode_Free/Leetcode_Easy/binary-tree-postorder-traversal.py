# Leetcode 145: Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal

from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(current_node):
            if not current_node:
                return []
            return dfs(current_node.left) + dfs(current_node.right) + [current_node.val]
        return dfs(root)
    