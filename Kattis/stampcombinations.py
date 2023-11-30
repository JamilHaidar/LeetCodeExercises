from collections import deque

m,n = list(map(int,input().split()))
a = list(map(int,input().split()))

left_sum = deque()
left_sum.append(a[0])
for elem in a[1:]:
    left_sum.append(left_sum[-1]+elem)

right_sum = deque()
right_sum.append(a[-1])
for elem in a[-2::-1]:
    right_sum.appendleft(right_sum[0]+elem)

print(left_sum)
print(right_sum)

# possible_vals = set()
# def dfs(l,r,current_val):  
#     if l>r:
#         return
#     if current_val not in possible_vals:
#         possible_vals.add(current_val)
    
#     dfs(l+1,r,current_val+a[l])
#     dfs(l,r-1,current_val+a[r])
# dfs(0,len(a)-1,0)

# for _ in range(n):
#     if int(input()) in possible_vals:
#         print('Yes')
#     else:
#         print('No')