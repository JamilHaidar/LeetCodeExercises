# Leetcode 104

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Recursive DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    # Iterative DFS
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     stack = [[root,1]]
    #     res = 0
    #     while stack:
    #         node,depth = stack.pop()
    #         if node:
    #             res = max(res,depth)
    #             stack.append([node.left,depth+1])
    #             stack.append([node.right,depth+1])
    #     return res

    # Iterative BFS
    # from collections import deque

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     q = deque()
    #     if root:
    #         q.append(root)
    
    #     res = 0
    #     while q:
    #         for _ in range(len(q)):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         res +=1
    #     return res