# Leetcode 21
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        head = output
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                output.next = list1
                list1 = list1.next
            else:
                output.next = list2
                list2 = list2.next
            output = output.next
        if list1==None:
            output.next = list2
        else:
            output.next = list1
        return head.next