import math
t = int(input())
prime_nums = dict()
def prime_helper(count):
    if count <2:return False
    for i in range(2,int(math.sqrt(count))+1):
        if count%i==0:return False
    return True

def is_prime(count):
    if count not in prime_nums: prime_nums[count] = prime_helper(count)
    return prime_nums[count]

for _ in range(t):
    n_flowers,distance = list(map(int,input().split()))
    prev_x = 0
    prev_y = 0
    current_x = 0
    current_y = 0
    flowers_so_far = 0
    for flower_idx in range(n_flowers):
        prev_x = current_x
        prev_y = current_y
        current_x,current_y = list(map(int,input().split()))
        distance -= math.sqrt((current_x-prev_x)**2 + (current_y-prev_y)**2)
        if distance>=0:flowers_so_far+=1
        else:
            for _ in range(n_flowers - flower_idx -1):input()
            break
    while not (flowers_so_far==0 or is_prime(flowers_so_far)):
        flowers_so_far -= 1
    print(flowers_so_far)