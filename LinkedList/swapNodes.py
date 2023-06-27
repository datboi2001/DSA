# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        :param head: head of the linked list
        :param k: position of the node from the beginning and end of the linked list
        :return: head of the linked list with the nodes swapped
        """
        copy_head = head
        count = 0
        kth_from_begin = None
        kth_before_begin = None
        while copy_head:
            count += 1
            if count == k:
                kth_from_begin = copy_head
            elif count == k -1:
                kth_before_begin = copy_head
            copy_head = copy_head.next
        kth_from_end = None
        kth_before_end = None
        end_position = count - k + 1
        copy_head = head
        cur_count = 0
        while copy_head:
            cur_count += 1
            if cur_count == end_position:
                kth_from_end = copy_head
            elif cur_count == end_position -1:
                kth_before_end = copy_head
            copy_head = copy_head.next
        if kth_from_begin == kth_from_end:
            return head
        if kth_before_begin:
            kth_before_begin.next = kth_from_end
        else:
            head = kth_from_end
        if kth_before_end:
            kth_before_end.next = kth_from_begin
        else:
            head = kth_from_begin
        # Swap the nodes
        temp = kth_from_begin.next
        kth_from_begin.next = kth_from_end.next
        kth_from_end.next = temp
        return head
