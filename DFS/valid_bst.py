import sys
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE

    def bst_utils(node: Node, min_value=float("-inf"), max_value=float("inf")) -> bool:
        # base case
        if node is None:
            # if node is None, it is a valid BST
            return True

        if not (min_value <= node.val <= max_value):
            return False

        return bst_utils(node.left, min_value, node.val) and bst_utils(node.right, node.val, max_value)
    return bst_utils(root)


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = valid_bst(root)
    print('true' if res else 'false')
