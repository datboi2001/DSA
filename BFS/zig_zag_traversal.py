from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag_traversal(root: Node) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    result = []
    queue = deque([root])
    odd = True
    while len(queue) > 0:
        cur_level = []
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            cur_level.append(node.val)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
        if not odd:
            cur_level.reverse()
        result.append(cur_level)
        odd = not odd
    return result


# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = zig_zag_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))
