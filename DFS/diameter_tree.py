from cloneTreeCorrespondingNode import TreeNode
from collections import deque

class Solution:

    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
        :param root: TreeNode
        :return: diameter of binary tree
        """
        # Idea: the diameter of a tree is the maximum of the following:
        # 1. the diameter of the left subtree
        # 2. the diameter of the right subtree
        # 3. the longest path that goes through the root node
        diameter = 0
        def recursion(root):
            nonlocal diameter
            if not root:
                return 0
            left = recursion(root.left)
            right = recursion(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        recursion(root)
        return diameter




