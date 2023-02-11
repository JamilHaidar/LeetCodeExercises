# Leetcode 23

from heapq import heappush,heappop
from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        first_elements = []
        for head_node in lists:
            if head_node:
                heappush(first_elements,head_node)
        root = ListNode()
        merged_list = root
        while first_elements:
            smallest_element = heappop(first_elements)
            merged_list.next = smallest_element
            merged_list = merged_list.next
            if smallest_element.next:
                heappush(first_elements,smallest_element.next)
        return root.next

def build_list(linked_list):
    if not linked_list:return None
    root = ListNode()
    current = root
    for element in linked_list[:-1]:
        current.val = element
        current.next = ListNode()
        current = current.next
    current.val = linked_list[-1]
    return root

def print_list(root):
    res = []
    while root:
        res.append(root.val)
        root = root.next
    print(res)

lists = [[1,4,5],[1,3,4],[2,6],[],[1]]

for i in range(len(lists)):
    lists[i] = build_list(lists[i])

# for elem in lists:
#     print_list(elem)

sol = Solution()
print_list(sol.mergeKLists(lists))
