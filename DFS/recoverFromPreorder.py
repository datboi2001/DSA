# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(node: Optional[TreeNode], level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        printTree(node.right, level + 1)


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        We run a preorder depth-first search (DFS) on the root of a binary tree.
At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
If a node has only one child, that child is guaranteed to be the left child.
Given the output traversal of this traversal, recover the tree and return its root.
        :param traversal: string of the traversal
        :return: root of the tree
        """
        # Solve with a stack
        stack = []
        i = 0
        while i < len(traversal):
            level = 0
            while traversal[i] == '-':
                level += 1
                i += 1
            value = 0
            while i < len(traversal) and traversal[i] != '-':
                value = value * 10 + int(traversal[i])
                i += 1
            node = TreeNode(value)
            if level == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                stack = stack[:level]
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None






tree = Solution().recoverFromPreorder("1-2--3--4-5--6--7")
printTree(tree)