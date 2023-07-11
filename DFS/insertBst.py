# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val:  int) -> Optional[TreeNode]:
        self.parent_node: Optional[TreeNode]  = None
        if not root:
            return TreeNode(val)
        def dfsInsert(node):
            if node:
                if val < node.val:
                    self.parent_node = node
                    dfsInsert(node.left)
                else:
                    self.parent_node = node
                    dfsInsert(node.right) 
        dfsInsert(root)
        if val < self.parent_node.val:
            self.parent_node.left = TreeNode(val)
        else:
            self.parent_node.right = TreeNode(val)
        return root


root = [4,2,7,1,3]
val = 5

def buildTree(arr):
    """
    :param root: array of integers
    """
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if arr[i]:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if arr[i]:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


print(Solution().insertIntoBST(buildTree(root), val))