nums = [1,2,3]
goal = min(nums)
res = 0
for elem in nums:
    res += elem-goal
print(res)