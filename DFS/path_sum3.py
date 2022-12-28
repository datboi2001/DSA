# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
       Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
        :param root: root of a binary tree
        :param targetSum: target sum
        :return: number of paths where the sum of the values along the path equals targetSum
        """
        # Idea: DFS
        if not root:
            return 0
        
        def dfs(node, target) -> int:
            # return the number of paths where the sum of the values along the path equals target
            if not node:
                return 0
            return int(node.val == target) + dfs(node.left, target - node.val) + dfs(node.right, target - node.val)
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
