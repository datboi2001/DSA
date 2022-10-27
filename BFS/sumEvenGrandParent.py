# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        :param root: root of a binary tree
        :return: sum of values of nodes with even-valued grandparent
        """
        total = 0
        if not root.left and not root.right:
            return total
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node.val % 2 == 0:
                if cur_node.left:
                    if cur_node.left.left:
                        total += cur_node.left.left.val
                    if cur_node.left.right:
                        total += cur_node.left.right.val
                if cur_node.right:
                    if cur_node.right.left:
                        total += cur_node.right.left.val
                    if cur_node.right.right:
                        total += cur_node.right.right.val
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        return total
