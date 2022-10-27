from collections import deque


from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    def tree_max_depth_recursion(root):
        if not root:
            return 0
        return max(tree_max_depth_recursion(root.left), tree_max_depth_recursion(root.right)) + 1

    return tree_max_depth_recursion(root)


def get_depth(root: Node) -> bool:
        if root is None:
            return 0
        height = 0
        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                front = queue.popleft()
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
        height += 1
        return height


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = tree_max_depth(root)
    print(res)
