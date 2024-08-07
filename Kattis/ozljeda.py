k = int(input())
xn = list(map(int,input().split()))
total = 0
l2r = [xn[0]]
for idx in range(k-1):
    l2r.append(l2r[idx]^xn[idx+1])
xn.append(l2r[-1])
l2r.append(0)

k += 1

q = int(input())
while q:
    l,r = list(map(int,input().split()))
    l -= 1
    r -= 1
    ans = 0
    ans ^= l2r[r%k]
    ans ^= l2r[l%k-1]
    print(ans)
    q -= 1