# Leetcode 563: Binary Tree Tilt
# https://leetcode.com/problems/binary-tree-tilt

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(current_node):
            if not current_node:
                return (0,0)
            left_sum,left_tilt = dfs(current_node.left)
            right_sum,right_tilt = dfs(current_node.right)
            node_tilt_sum = abs(left_sum-right_sum)
            return (left_sum+right_sum+current_node.val,left_tilt+right_tilt+node_tilt_sum)
        _,total_tilt = dfs(root)
        return total_tilt