# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        :param root: The root of a binary tree
        :return: True if the binary tree is symmetric, otherwise return False
        """
        if root is None:
            return True
        # Idea: Use a recursive function to check if the binary tree is symmetric.
        # The main idea is that we use a recursive function to check if the binary tree is symmetric. We use a helper
        # function to check if the left subtree is symmetric to the right subtree. This helper function takes two
        # parameters: the left subtree and the right subtree. If the left subtree is None and the right subtree is None,
        # we return True. If the left subtree is None or the right subtree is None, we return False. If the value of the
        # left subtree is not equal to the value of the right subtree, we return False. Otherwise, we return the result
        # of the helper function called recursively on the left subtree and the right subtree. 

        def recursion(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return recursion(left.left, right.right) and recursion(left.right, right.left)
        
        return recursion(root.left, root.right)

    