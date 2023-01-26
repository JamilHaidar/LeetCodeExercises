# Leetcode 124

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.path = root.val
        
        def max_path(root):
            if not root:
                return 0
           
            left = max(max_path(root.left),0)
            right = max(max_path(root.right),0)
            self.path = max(left + right + root.val, self.path)
                
            return max(left, right) + root.val
            
        max_path(root)
        return self.path