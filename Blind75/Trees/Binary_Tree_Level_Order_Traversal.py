# Leetcode 102

from typing import Optional,List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if root:
            q.append(root)
        while q:
            res.append([elem.val for elem in q])
            for _ in range(len(q)):
                elem = q.popleft()
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
        return res            