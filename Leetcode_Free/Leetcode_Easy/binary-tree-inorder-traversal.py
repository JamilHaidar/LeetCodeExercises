# Leetcode 94: Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal

from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Recursive
        # def dfs(current_node):
        #     if not current_node:
        #         return []
        #     return dfs(current_node.left) + [current_node.val] + dfs(current_node.right)
        # return dfs(root)
    
        #Iterative
        if not root:return []
        current_node = root
        stack = []
        ans = []
        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            
            current_node = stack.pop()
            ans.append(current_node.val)
            current_node = current_node.right
        return ans