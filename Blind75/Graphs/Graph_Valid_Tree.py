# Leetcode 261

from typing import List
from collections import defaultdict
class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:return n==1
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        def checkCycle(current_node,prevNode):
            if current_node in visited:return True
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor==prevNode:continue
                if checkCycle(neighbor,current_node):return True
            return False
        if checkCycle(edges[0][0],edges[0][0]):return False
        return len(visited)==n

sol = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(sol.valid_tree(n,edges))