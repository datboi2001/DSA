# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
        def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            """
            :param head: head of the linked list
            :return: head of the sorted linked list
            """
            if not head:
                return None
            # Put all nodes in a priority queue
            copy_head = head
            pq = []
            while copy_head:
                pq.append(copy_head)
                copy_head = copy_head.next
            # Create a new linked list with the sorted values
            pq.sort(key=lambda x: x.val, reverse=True)
            new_head = pq.pop()
            copy_head = new_head
            while len(pq) > 0:
                copy_head.next = pq.pop()
                copy_head = copy_head.next
            copy_head.next = None
            return new_head