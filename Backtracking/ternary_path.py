from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE

    def dfs(root: Node, path: List[str], res: List[str]):
        if all(c is None for c in root.children):
            res.append('->'.join(path) + f"->{root.val}")
            return
        for child in root.children:
            if child is not None:
                path.append(f"{root.val}")
                dfs(child, path, res)
                path.pop()

    all_paths = []
    if root:
        dfs(root, [], all_paths)
    return all_paths

# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
