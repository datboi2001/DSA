class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    i = j = head
    while j and j.next:
        i = i.next
        j = j.next.next
    return i.val
def build_list(nodes, f):
    val = next(nodes, None)
    if val is None: return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

if __name__ == '__main__':
    head = build_list(iter(input().split()), int)
    res = middle_of_linked_list(head)
    print(res)
