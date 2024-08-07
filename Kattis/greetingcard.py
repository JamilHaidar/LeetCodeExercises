# Only integer pairs that give separation are:
# 0 2018.0
# 1118 1680.0
offsets = [(0,2018),(2018,0),(1118,1680),(1680,1118)]
n = int(input())
points = set()
for _ in range(n):
    points.add(tuple(map(int,input().split())))

count = 0
for x,y in points:
    for dx,dy in offsets:
        if (x+dx,y+dy) in points:
            count += 1
        if dx>0 and dy>0:
            if (x-dx,y+dy) in points:
                count += 1
print(count)