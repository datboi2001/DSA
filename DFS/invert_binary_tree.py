from typing import Optional
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    # WRITE YOUR BRILLIANT CODE HERE
    if tree is None:
        return None
    tree.left, tree.right = invert_binary_tree(tree.right), invert_binary_tree(tree.left)
    return tree




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        returnRoot = root
        queue = deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return returnRoot   
             

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = invert_binary_tree(tree)
    print(' '.join(format_tree(res)))
