from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        :param root: TreeNode
        The values of exactly 2 nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
        Do not return anything, modify root in-place instead.
        """
        # Main idea: inorder traversal
        # Time: O(n), space: O(n)

        # inorder traversal
        self.res = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.res.append(root)
                inorder(root.right)
        
        inorder(root)
        # find the two nodes that are swapped
        x, y = None, None
        for i in range(len(self.res) - 1):
            if self.res[i].val > self.res[i + 1].val:
                y = self.res[i + 1]
                # the first time we find the swapped node, we set x to be the previous node
                if not x:
                    x = self.res[i]
                else:
                    break
        # swap the values of the two nodes
        x.val, y.val = y.val, x.val