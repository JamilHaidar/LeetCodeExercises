# Leetcode 110: Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:return True
        def dfs(current_node):
            if not current_node:
                return (0,True)
            right_val,right_height_balanced = dfs(current_node.right)
            left_val,left_height_balanced = dfs(current_node.left)
            return 1+max(right_val,left_val), (right_height_balanced and left_height_balanced) and (abs(left_val-right_val)<=1)
        
        _,height_balanced = dfs(root)
        return height_balanced
    
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:

#         def dfs(current_node):
#             if not current_node:
#                 return 0
#             current_node.val = 1+max(dfs(current_node.right),dfs(current_node.left))
#             return current_node.val
        
#         dfs(root)
        
#         queue = deque() 
#         queue.append(root)
#         while queue:
#             depth_nodes = len(queue)
#             subtree_depth = queue[0].val
#             for _ in range(depth_nodes):
#                 current_node = queue.popleft()
#                 if current_node.val != subtree_depth:
#                     return False
#                 if current_node.left:
#                     queue.append(current_node.left)
#                 if current_node.right:
#                     queue.append(current_node.right)
#         return True