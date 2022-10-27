class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def has_cycle(nodes: Node) -> bool:
    # Check if nodes has a cycle
    slow = nodes;
    fast = nodes.next;

    while fast.next is not None and fast.next.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

if __name__ == '__main__':
    raw_input = [int(x) for x in input().split()]
    nodes_list = []
    for i, entry in enumerate(raw_input):
        nodes_list.append(Node(i))
    for i, entry in enumerate(raw_input):
        if entry != -1:
            nodes_list[i].next = nodes_list[entry]
    nodes = nodes_list[0]
    res = has_cycle(nodes)
    print('true' if res else 'false')
