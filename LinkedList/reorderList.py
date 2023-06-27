class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        You are given the head of a singly linked-list. The list can be represented as:
        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:
        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        Do not return anything, modify head in-place instead.
        :param head: head of a singly linked-list
        """
        # Main idea: use two pointers. One pointer is used to iterate through the list, and the other pointer is used to
        # keep track of the position to insert the next element that is not equal to val.

        if not head:
            return None
        
        # Find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # Merge the two halves
        first = head
        second = prev
        while second.next:
            next = first.next
            first.next = second
            first = next
            next = second.next
            second.next = first
            second = next

# Path: LinkedList\reverseList.py
        