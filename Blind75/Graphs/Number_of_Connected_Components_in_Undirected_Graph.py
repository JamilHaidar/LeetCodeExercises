# Leetcode 323

from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.f = {}

    def findParent(self, x):
        y = self.f.get(x, x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x, y):
        self.f[self.findParent(x)] = self.findParent(y)

class Solution:
    def countComponentsDFS(self,n: int, edges: List[List[int]]) -> int:
        # O(E+V)
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        def dfs(current_node):
            if current_node in visited:return
            visited.add(current_node)
            for neighbor in graph[current_node]:
                dfs(neighbor)
        count = 0
        for node in range(n):
            if node in visited:continue
            count +=1
            dfs(node)
        return count
    def countComponentsUnionFind(self,n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n
        
        def find(current_node):
            res = current_node
            while res!=parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(node_a,node_b):
            parent_a,parent_b = find(node_a),find(node_b)
            if parent_a == parent_b: return 0
            if rank[parent_b]>rank[parent_a]:
                parent[parent_a] = parent_b
                rank[parent_b] += rank[parent_a]
            else:
                parent[parent_b] = parent_a
                rank[parent_a] += rank[parent_b]
            return 1

        count=n
        for node_a, node_b in edges:
            count -= union(node_a,node_b)
        return count

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a, b)
        return len(set(dsu.findParent(x) for x in range(n)))

n=5
edges = [[0,1],[1,2],[3,4]]
sol = Solution()

print(sol.countComponentsDFS(n,edges))
print(sol.countComponentsUnionFind(n,edges))
print(sol.countComponents(n,edges))