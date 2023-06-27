# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from heapq import heappop, heappush
from typing import Optional, List
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        if not lists or all(ll is None for ll in lists):
            return None
        ListNode.__lt__ = lambda self, other: self.val < other.val
        ListNode.__le__ = lambda self, other: self.val <= other.val
        copy_res = res
        heap = []
        for cur_list in lists:
            if cur_list:
                heappush(heap, (cur_list.val, cur_list))
        while len(heap) > 0:
            val, current_list = heappop(heap)
            copy_res.val = val
            current_list = current_list.next
            if current_list:
                heappush(heap, (current_list.val, current_list))
            if len(heap) > 0:
                copy_res.next = ListNode()
                copy_res = copy_res.next
        return res

def convert_to_linkedList(array: list[int]) -> ListNode | None:
    if len(array) == 0:
        return None
    old_node = ListNode()
    return_node = old_node
    for i in range(len(array)):
        old_node.val = array[i]
        if i != len(array) - 1:
            old_node.next = ListNode()
        else:
            break
        old_node = old_node.next
    return return_node

def print_linkedList(head: ListNode):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    lists = [[1,4,5], [1,3,4], [2,6]]
    lists = [convert_to_linkedList(i) for i in lists]
    result = Solution().mergeKLists(lists)
    print_linkedList(result)