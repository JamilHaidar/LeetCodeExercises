from collections import defaultdict
import math
n,m = list(map(int,input().split()))
start_pos,end_pos = list(map(int,input().split()))
undirected_graph = defaultdict(list)
for _ in range(m):
    planet_1,planet_2 = list(map(int,input().split()))
    undirected_graph[planet_1].append(planet_2)
    undirected_graph[planet_2].append(planet_1)

queue = [(start_pos,0)]
visited = set()
while queue:
    current_node = queue.pop(0)
    if current_node[0]==end_pos:
        print(int(math.ceil(current_node[1]/2)))
        break
    visited.add(current_node[0])
    for neighbor in undirected_graph[current_node[0]]:
        if neighbor not in visited:
            queue.append((neighbor,current_node[1]+1))