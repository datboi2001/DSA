from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.flag = False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if hasattr(head, "flag") and head.flag:
                return True
            head.flag = True
            head = head.next
        return False