# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> Optional[TreeNode]:
        """
        Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node
        in the tree is now the root of the tree, and every node has no left child and only one right child.
        :param root: root of the tree 
        :return: the root of the tree after rearranging
        """
        # Idea: DFS on the tree and create a new tree
        # Time complexity: O(n)
        # Space complexity: O(n)
        if not root:
            return None
        self.res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        new_root = TreeNode(self.res[0])
        cur = new_root
        for i in range(1, len(self.res)):
            cur.right = TreeNode(self.res[i])
            cur = cur.right
        return new_root

            