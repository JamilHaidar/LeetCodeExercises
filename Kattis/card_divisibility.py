l,r = list(map(int,input().split()))
print((r+l)*(r-l+1)*5 %9)