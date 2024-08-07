# Leetcode 637: Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree
# Definition for a binary tree node.
from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        # dfs approach

        # stack = [[root,0]]
        # sum_nodes = []
        # num_nodes = []
        # while stack:
        #     current_node,level = stack.pop()
        #     if level == len(sum_nodes): 
        #         sum_nodes.append(current_node.val)
        #         num_nodes.append(1)
        #     else:
        #         sum_nodes[level] += current_node.val
        #         num_nodes[level] += 1

        #     if current_node.left:
        #         stack.append([current_node.left,level+1])

        #     if current_node.right:
        #         stack.append([current_node.right,level+1])
        # ans = []
        # for index in range(len(sum_nodes)):
        #     ans.append(sum_nodes[index]/num_nodes[index])
        # return ans

        # bfs approach
        
        from collections import deque
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            sum_nodes = 0
            num_nodes = len(queue)
            for _ in range(num_nodes):
                current_node = queue.popleft()
                sum_nodes += current_node.val

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)
            res.append(sum_nodes/num_nodes)
        return res