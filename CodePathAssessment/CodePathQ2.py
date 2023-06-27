def sum_of_left_leaves(root):
    """
    Write your code here
    :type root: TreeNode
    :rtype: int
    """
    sum_leaves = 0
    def sum_left_leaves_rec(root, isleftLeaf):
        nonlocal sum_leaves
        if root is None:
            return
        if root.left is None and root.right is None and isleftLeaf:
            sum_leaves += root.val
        sum_left_leaves_rec(root.left, 1)
        sum_left_leaves_rec(root.right, 0)
    sum_left_leaves_rec(root, 0)
    return sum_leaves