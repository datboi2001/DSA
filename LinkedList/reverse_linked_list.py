# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        next_node = None
        while curr is not None:
            # Store next node
            next_node = curr.next
            # Change next of current. This is where the reversing happens
            curr.next = prev
            # Move prev and curr one step forward
            prev = curr
            curr = next_node
        return prev
            