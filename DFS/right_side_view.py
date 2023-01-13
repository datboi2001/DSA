# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        """
        :param root: The root of a binary tree
        :return: The right side view of the binary tree
        """
        # Idea: Use a right-side recursion to find the right side view of the binary tree.
        # The main idea is that we use a right-side recursion to find the right side view of the binary tree.
        results = []
        def right_side_recursion(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return
            # If the level is equal to the length of the results, we append the value of the root to the results.
            if level == len(results):
                results.append(root.val)
            # We use a right-side recursion to find the right side view of the binary tree.
            right_side_recursion(root.right, level + 1)
            right_side_recursion(root.left, level + 1)
        
        right_side_recursion(root, 0)
        return results

tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(Solution().rightSideView(tree))