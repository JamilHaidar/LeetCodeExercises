# Leetcode 257: Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths

from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # def dfs(current_node):            
        #     if not current_node.left and not current_node.right:
        #         return [str(current_node.val)]
        #     ans = []
        #     if current_node.left:
        #         ans = ans + [str(current_node.val)+'->'+elem for elem in dfs(current_node.left)]
        #     if current_node.right:
        #         ans = ans + [str(current_node.val)+'->'+elem for elem in dfs(current_node.right)]
        #     return ans
        # return dfs(root)

        

        ans = []
        def dfs(current_node,current_path):
            if not current_node.left and not current_node.right:
                return ans.append(current_path+str(current_node.val))
            else:
                current_path += str(current_node.val)+"->"
                if current_node.left:
                    dfs(current_node.left,current_path)
                if current_node.right:
                    dfs(current_node.right,current_path)
        dfs(root,"")
        return ans