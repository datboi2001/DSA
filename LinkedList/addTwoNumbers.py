from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = sum_result = ListNode(0)
        digit_sum = 0
        while l1 or l2:
            # Edge cases
            if l2:
                digit_sum += l2.val
                l2 = l2.next
            if l1:
                digit_sum += l1.val
                l1 = l1.next
                # Add two numbers
            sum_result.next = ListNode(digit_sum % 10)
            digit_sum = 0 if digit_sum < 10 else 1
            sum_result = sum_result.next
        if digit_sum:
            sum_result.next = ListNode(digit_sum)
        return result.next

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ll = 0
    # Convert linked list to numbers and add them together
        for ll in [l1, l2]:
            integer = 0
            base_10 = 1
            while ll is not None:
                integer += ll.val * base_10
                ll = ll.next
                base_10 *= 10
            sum_ll += integer
        result_ll = ListNode()
        copy_result_ll = result_ll
        # Convert sum to linked list
        while sum_ll > 0:
            digit = sum_ll % 10
            copy_result_ll.val = digit
            sum_ll //= 10
            if sum_ll > 0:
                copy_result_ll.next = ListNode()
                copy_result_ll = copy_result_ll.next
        return result_ll


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
Solution().addTwoNumbers(l1, l2)