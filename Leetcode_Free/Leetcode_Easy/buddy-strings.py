# Leetcode 859: Buddy Strings
# https://leetcode.com/problems/buddy-strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # if len(s)!=len(goal):return False
        # if s==goal:
        #     return len(set(s))!=len(s)
        # current_index = 0
        # is_swap = False
        # to_swap = ['','']
        # finished_swap = False
        # while current_index<len(s):
        #     if s[current_index] != goal[current_index]:
        #         if finished_swap:
        #             return False
        #         if not is_swap:
        #             is_swap = True
        #             to_swap = [goal[current_index],s[current_index]]
        #         else:
        #             if s[current_index]==to_swap[0] and goal[current_index]==to_swap[1]:
        #                 finished_swap = True
        #             else:
        #                 return False
        #     current_index += 1
        
        # return finished_swap

        if len(s)!=len(goal):return False
        if s==goal: return len(set(s))!=len(s)
        diff = [(i,j) for i,j in zip(s,goal) if i!=j]
        return len(diff)==2 and diff[0] == diff[1][::-1]