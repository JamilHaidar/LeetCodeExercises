# Leetcode 297
# Note: I was able to recreate the same encoding Leetcode uses for serialization and deserialization
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = deque()
        q.append(root)
        while q:
            final_layer = True
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left or node.right:final_layer=False
                    q.append(node.left)
                    q.append(node.right)
                    temp.append(str(node.val))
                else:
                    temp.append(str(None))
            if final_layer:
                while temp:
                    if temp[-1]=='None':
                        temp.pop()
                    else:
                        break
            res = res+temp
            if final_layer:break
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:return None
        def create_node(val):
            if val=='None':
                return None
            else:
                return TreeNode(int(val))

        data = data.split(',')
        root = create_node(data.pop(0))

        q = deque()
        q.append(root)

        while data:
            for _ in range(len(q)):
                current_node = q.popleft()
                if not data:break
                left_node = create_node(data.pop(0))
                current_node.left = left_node
                if not data:break
                right_node = create_node(data.pop(0))
                current_node.right = right_node
                if left_node:q.append(left_node)
                if right_node:q.append(right_node)
        return root

ser = Codec()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
# root.right.right.left = TreeNode(6)
root.right.left.left = TreeNode(6)
print(ser.serialize(root))