# Leetcode 133

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: Node) -> Node:
        # mapping = dict()
        # def dfs(current_node):
        #     if current_node in mapping:return mapping[current_node]
        #     mapping[current_node] = Node(current_node.val)
            
        #     for neighbor in current_node.neighbors:
        #         mapping[current_node].neighbors.append(dfs(neighbor))
        #     return mapping[current_node]
        # return dfs(node)
        if not node: return node

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val)
        self.visited[node] = clone_node
        if node.neighbors:clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

sol = Solution()

# Build graph
root = Node(1)
root.neighbors.append(Node(2))
root.neighbors.append(Node(4))
root.neighbors[0].neighbors.append(root)
root.neighbors[0].neighbors.append(Node(3))
root.neighbors[1].neighbors.append(root)
root.neighbors[1].neighbors.append(root.neighbors[0].neighbors[1])
root.neighbors[0].neighbors[1].neighbors.append(root.neighbors[0])
root.neighbors[0].neighbors[1].neighbors.append(root.neighbors[1])

def print_graph(root):
    # dfs print graph adjacency list
    stack = [root]
    seen = set()
    while stack:
        curr = stack.pop()
        if curr in seen:continue
        seen.add(curr)
        print(f'{curr.val}: {[elem.val for elem in curr.neighbors]}')
        for elem in curr.neighbors:
            stack.append(elem)

print_graph(root)
print()
print_graph(sol.cloneGraph(root))


