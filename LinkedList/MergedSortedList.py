# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        old_node = ListNode()
        return_node = old_node
        while list1 or list2:
            if list1 and list2:
                if list1.val >= list2.val:
                    node_value = list2.val
                    list2 = list2.next
                else:
                    node_value = list1.val
                    list1 = list1.next
            elif list1:
                node_value = list1.val
                list1 = list1.next
            else:
                node_value = list2.val
                list2 = list2.next
            old_node.val = node_value
            if list1 is not None or list2 is not None:
                old_node.next = ListNode()
            else:
                break
            old_node = old_node.next
        return return_node