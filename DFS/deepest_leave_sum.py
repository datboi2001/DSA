# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
class Solution:
    def tree_max_depth(self, root):
        if not root:
            return 0
        queue = deque([root])
        max_depth = 0
        while len(queue) > 0:
            max_depth += 1
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
        return max_depth

    def is_max_depth(self, node, max_depth) -> bool:
        return node.depth == max_depth
  
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        max_depth = self.tree_max_depth(root)
        root.depth = 1
        stack = [root]
        while len(stack) > 0:
            cur_node = stack.pop()
            if self.is_max_depth(cur_node, max_depth):
                total += cur_node.val
            if (cur_node.left):
                cur_node.left.depth = cur_node.depth + 1
                stack.append(cur_node.left)
            if (cur_node.right):
                cur_node.right.depth = cur_node.depth + 1
                stack.append(cur_node.right)
        return total