# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        :param head: ListNode the head of the linked list
        :param k: int the number of rotations
        :return: ListNode the head of the rotated linked list
        """
        # Main idea: Calculate the length of the list
        # Then, calculate the new node that will be the head
        # Then, rotate the list

        # Edge case: The list is empty
        if not head:
            return None
        if head and head.next is None:
            return head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # Edge case: k is a multiple of the length
        k = k % length

        # Edge case: k is 0
        if k == 0:
            return head
        
        # Find the new head
        new_head = head
        for i in range(length - k - 1):
            new_head = new_head.next
        # Find the new tail
        new_tail = new_head
        while new_tail.next:
            new_tail = new_tail.next
        # Rotate the list
        new_tail.next = head
        head = new_head.next
        new_head.next = None
        return head

        



        
