n = int(input())
pillars = []
for _ in range(n):
    pillars.append(tuple(map(int,input().split())))
pillars = sorted(pillars)

# First solution O(10001*n)
ground = [0]*10001
total_length = 0
for pillar in pillars:
    total_length += pillar[0] - ground[pillar[1]]
    total_length += pillar[0] - ground[pillar[2]-1]
    for idx in range(pillar[1],pillar[2]):
        ground[idx] = pillar[0]
print(total_length)

# Second solution O(n^2)
# total_length = 0
# for pillar_index in range(n):
#     height,left,right = pillars[pillar_index]
#     left_done = False
#     right_done = False
#     if pillar_index > 0:    
#         for previous_pillar in pillars[pillar_index-1::-1]:
#             if not left_done:
#                 if previous_pillar[1]<=left<previous_pillar[2]:
#                     left_done = True
#                     total_length += height - previous_pillar[0]
#             if not right_done:
#                 if previous_pillar[1]<right<=previous_pillar[2]:
#                     right_done = True
#                     total_length += height - previous_pillar[0]
#             if left_done and right_done:break
#     if not left_done:
#         total_length += height
#     if not right_done:
#         total_length += height
# print(total_length)