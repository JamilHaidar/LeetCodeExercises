# 5 = 101
# 6 = 110
# 7 = 111
# a = 100 = 4
left = 5
right = 7
def rangeBitwiseAnd(left: int, right: int) -> int: 
    bit_shifts = 0
    while left<right:
        left >>= 1
        right >>= 1
        bit_shifts +=1
    return left << bit_shifts
print(rangeBitwiseAnd(left,right))