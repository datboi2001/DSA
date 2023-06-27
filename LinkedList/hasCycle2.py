from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :param head: head of the linked list
        :return: the node where the cycle begins
        """
        if not head:
            return None
        while head:
            if hasattr(head, "flag") and head.flag:
                return head
            head.flag = True
            head = head.next 
def detectCycleII(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    :param head: head of the linked list
    :return: the node where the cycle begins
    """
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    slow = head
    while slow != fast:
        # slow and fast will meet at the beginning of the cycle
        slow = slow.next
        fast = fast.next
    return slow


def createLinkedListWithCycle(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    node.next = head
    return head

ll_with_cycle = createLinkedListWithCycle([3, 2, 0, -4])

print(Solution().detectCycle(ll_with_cycle))
# print(detectCycleII(ll_with_cycle))