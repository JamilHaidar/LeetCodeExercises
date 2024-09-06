# Leetcode 144: Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(current_node):
            if not current_node:
                return []
            return [current_node.val] + dfs(current_node.left) + dfs(current_node.right)
        return dfs(root)