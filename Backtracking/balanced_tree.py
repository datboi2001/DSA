class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def treeHeight(root):
            if not root:
                return 0
            queue = deque([root])
            height = 0
            while queue:
                n = len(queue)
                for i in range(n):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                height += 1
            return height 
        if not root:
            return True
        return abs(treeHeight(root.left) - treeHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)