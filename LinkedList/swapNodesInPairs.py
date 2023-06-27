class Listnode:
    def __init__(self, val=0, next=none):
        self.val = val
        self.next = next

def print_list(head: listnode):
    while head:
        print(head.val, sep=" ")
        head = head.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        first_pair = True
        copy_head = head
        temp = None
        prev_node = None
        while True:
            if not copy_head.next:
                break
            second_node = copy_head.next
            third_node = second_node.next
            second_node.next = copy_head
            copy_head.next = third_node
            if prev_node:
                prev_node.next = second_node
            if first_pair:
                temp = second_node
                first_pair = False
            if third_node is None:
                break
            else:
                prev_node = copy_head
                copy_head = copy_head.next
        return temp or head 

print_list(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3)))))
        
