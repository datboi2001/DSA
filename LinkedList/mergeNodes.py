# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print()

from typing import Optional
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        """
        :param head: head of a linked list
        :return: head of a linked list where all nodes with value 0 are removed and all other nodes are merged
        """
        # Main idea: we use a dummy node to point to the head of the linked list. We traverse the linked list and
        # remove all nodes with value 0. We merge all other nodes.
        # Time complexity: O(n)
        # Space complexity: O(1)
        head = head.next
        return_node = ListNode(head.val)
        copy_return_node = return_node
        head = head.next
        while head:
            if head.val != 0:
                copy_return_node.val += head.val
            else:
                if head.next is None:
                    break
                copy_return_node.next = ListNode()
                copy_return_node = copy_return_node.next
            head = head.next
        if copy_return_node.val == 0:
            copy_return_node = None
        return return_node


if __name__ == '__main__':
    ll = ListNode(0, ListNode(1, ListNode(0, ListNode(2, ListNode(0, ListNode(3, ListNode(0, ListNode(4))))))))
    new_ll = Solution().mergeNodes(ll)
    print_list(new_ll)
