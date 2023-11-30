from collections import defaultdict
from heapq import *

n,m,f,s,t = list(map(int,input().split()))
graph = defaultdict(list)

for _ in range(m):
    i,j,c = list(map(int,input().split()))
    graph[i].append((c,j))
    graph[j].append((c,i))

flights = []
for _ in range(f):
    u,v = list(map(int,input().split()))
    flights.append((u,v))

def dijkstra(graph,start):
    q = [(0, start)]
    visited = set()
    mins = {start: 0}
    while(q):
        (total_cost,v1) = heappop(q)
        if v1 not in visited:
            visited.add(v1)
            for cost,v2 in graph.get(v1,()):
                if v2 in visited:
                    continue
                previous_cost = mins.get(v2,None)
                next_cost = total_cost + cost
                if previous_cost is None or next_cost < previous_cost:
                    mins[v2] = next_cost
                    heappush(q,(next_cost,v2))
    return mins

distance_from_s = dijkstra(graph,s) # s[v] shortest distance from s to v using dijkstra
distance_from_t = dijkstra(graph,t) # t[v] shortest distance from t to v (basically also v to t) using dijkstra
min_distance = distance_from_s.get(t,50001)
for u,v in flights:
    if u in distance_from_s and v in distance_from_t:
        min_distance = min(min_distance,distance_from_s[u]+distance_from_t[v])
print(min_distance)