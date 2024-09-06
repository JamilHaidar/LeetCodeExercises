class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n
    def find(self,u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_v] > self.rank[root_u]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

n,m,q = list(map(int,input().split()))

roads = set()
for _ in range(m):
    roads.add(tuple(map(int,input().split())))

queries = []
for _ in range(q):
    t,u,v = list(map(int,input().split()))
    if t==0:
        if (u,v) in roads:
            roads.remove((u,v))
    queries.append((t,u,v))

road_connections = UnionFind(n)
for safe_u,safe_v in roads:
    road_connections.union(safe_u,safe_v)

results = []
for t,u,v in reversed(queries):
    if t==1:
        if road_connections.find(u) == road_connections.find(v):
            results.append('safe')
        else:
            results.append('unsafe')
    else:
        road_connections.union(u,v)

for elem in reversed(results):
    print(elem)