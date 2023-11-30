directions = [(-1,-1),(-1,0),(-1,1),
        (0,-1),(0,1),
        (1,-1),(1,0),(1,1),]
output = [0]*9
n_r,n_c = list(map(int,input().split()))
seat_count = [0 for _ in range(n_r*n_c)]
n = int(input())
attendees = []
for _ in range(n):
    r,c = list(map(int,input().split()))
    r -= 1
    c -= 1
    attendees.append(r*n_c+c)
    for direction in directions:
        if 0 <= r+direction[0] < n_r and 0 <= c+direction[1] < n_c:seat_count[(r+direction[0])*n_c+c+direction[1]] +=1

for attendee in attendees:
    output[seat_count[attendee]]+=1
print(' '.join([str(elem) for elem in output]))