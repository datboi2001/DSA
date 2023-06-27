from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_min_depth(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    depth = -1
    queue = deque([root])
    while len(queue) > 0:
        depth += 1
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if not node.left and not node.right:
                return depth
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
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
    res = binary_tree_min_depth(root)
    print(res)
