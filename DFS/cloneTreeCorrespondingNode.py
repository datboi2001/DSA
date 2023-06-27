# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original.left and not original.right:
            return cloned
        original_stack = [original]
        cloned_stack = [cloned]
        while original_stack and cloned_stack:
            original_node = original_stack.pop()
            cloned_node = cloned_stack.pop()
            if original_node == target:
                return cloned_node
            if original_node.left:
                original_stack.append(original_node.left)
                cloned_stack.append(cloned_node.left)
            if original_node.right:
                original_stack.append(original_node.right)
                cloned_stack.append(cloned_node.right)
