class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: Node) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    if root is None:
        return 'x '
    return f"{root.val} " + serialize(root.left) + serialize(root.right)


def deserialize(s: str) -> Node:
    # AND HERE
    def build_tree(nodes) -> Node | None:
        val = next(nodes)
        if not val or val == 'x':
            return None
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    return build_tree(iter(s.split()))

if __name__ == '__main__':
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    def print_tree(root):
        if not root:
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)
    root = build_tree(iter(input().split()))
    new_root = deserialize(serialize(root))
    print(' '.join(print_tree(new_root)))
