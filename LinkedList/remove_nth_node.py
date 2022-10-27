# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None
        copy_head = head
        sz = 0
        while copy_head:
            sz += 1
            copy_head = copy_head.next
        n = sz - n + 1
        if n == 1:
            return head.next
        copy_head = head
        count = 1
        while copy_head:
            if count == n - 1:
                copy_head.next = copy_head.next.next
                break
            count += 1
            copy_head = copy_head.next
        return head


print(Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2))