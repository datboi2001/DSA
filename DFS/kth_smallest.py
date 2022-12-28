# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        :root: root of a binary search tree.
        :k: an integer.
        :return: the kth smallest element in the BST.
        """
        # Idea: in-order traversal.

        if root and not root.left and not root.right:
            return root.val
        
        # In-order traversal.
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

# Time complexity: O(n)
# Space complexity: O(n)