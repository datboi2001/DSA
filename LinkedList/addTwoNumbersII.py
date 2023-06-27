# Definition for singly-linked list.
from typing import Optional
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ll = 0
        for ll in [l1, l2]:
            integer = 0
            while ll:
                integer *= 10
                integer += ll.val
                ll = ll.next
            sum_ll += integer
        result_ll = ListNode(0)
        if sum_ll == 0:
            return result_ll
        # Convert sum to linked list
        while sum_ll:
            # Get rightmost digit then construct linked list from right to left
            digit, sum_ll = sum_ll % 10, sum_ll // 10
            result_ll.next = ListNode(digit, result_ll.next)
        return result_ll.next


l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(Solution().addTwoNumbers(l1, l2))