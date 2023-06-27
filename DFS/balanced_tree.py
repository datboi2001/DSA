class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(tree: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    def tree_height(root: Node) -> int:
        if root is None:
            return 0
        return max(tree_height(root.left), tree_height(root.right)) + 1

    if tree is None:
        return True

    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)

    if abs(left_height - right_height) <= 1 and is_balanced(tree.left) and is_balanced(tree.right):
        return True
    return False


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x':
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')
