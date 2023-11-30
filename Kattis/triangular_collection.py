import bisect
n = int(input())
side_lengths = []
for _ in range(n):
    bisect.insort(side_lengths,int(input()))
count = 0
# print(side_lengths)
# for first_side_index in range(n-2):
#     third_side_index = first_side_index + 2
#     for second_side_index in range(first_side_index+1,n):
#         # print('pre',side_lengths[first_side_index] , side_lengths[second_side_index] , side_lengths[third_side_index] if third_side_index<n else str(third_side_index)+" index")
#         while (third_side_index < n and side_lengths[first_side_index] + side_lengths[second_side_index] > side_lengths[third_side_index]):
#             third_side_index += 1
#         # print('pos',side_lengths[first_side_index] , side_lengths[second_side_index] , side_lengths[third_side_index] if third_side_index<n else str(third_side_index)+" index")
#         if third_side_index > second_side_index:
#             count += third_side_index - second_side_index - 1
#             # print(third_side_index - second_side_index - 1)

# for largest_side_index in range(n-1, 0 ,-1):
#     smallest_side_index = 0
#     middle_side_index = largest_side_index - 1

#     while(smallest_side_index < middle_side_index):
#         if side_lengths[smallest_side_index]+side_lengths[middle_side_index] > side_lengths[largest_side_index]:
#             count += middle_side_index - smallest_side_index
#             print(side_lengths[smallest_side_index],side_lengths[middle_side_index] , side_lengths[largest_side_index],middle_side_index - smallest_side_index)
#             middle_side_index -= 1
#         else:
#             smallest_side_index += 1

for first_side_index in range(n):
    for second_side_index in range(first_side_index+1,n):
        largest_possible_side = side_lengths[first_side_index] + side_lengths[second_side_index]
        number_of_subsets = 0
        third_side_index = second_side_index + 1
        while (third_side_index < n and largest_possible_side > side_lengths[third_side_index]):
            third_side_index += 1
            number_of_subsets = number_of_subsets*2 + 1
        count += number_of_subsets

print(count)