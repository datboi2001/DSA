class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    def visible_recursion(current: Node, max_sofar: int or float):
        """

        :param current: The current tree node that we are processing
        :param max_sofar: The maximum value we encountered from the root to the current node
        """
        if current is None:
            return 0
        total = 0
        if current.val >= max_sofar:
            total += 1
        total += visible_recursion(current.left, max(max_sofar, root.val))
        total += visible_recursion(current.right, max(max_sofar, root.val))
        return total
    return visible_recursion(root, -float("inf"))

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)
