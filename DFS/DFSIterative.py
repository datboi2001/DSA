# Python program to perform iterative preorder traversal

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# An iterative process to print preorder traversal of BT
def iterativePreorder(root):
    # Base CAse
    if root is None:
        return

    # create an empty stack and push root to it
    nodeStack = [root]

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while len(nodeStack) > 0:

        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print(node.data, end=" ")

        # Push right and left children of the popped node
        # to stack
        if node.right:
            nodeStack.append(node.right)
        if node.left:
            nodeStack.append(node.left)
    print()


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


# A iterative function to do postorder traversal of
# a given binary tree
def postOrderIterative(root):

    if root is None:
        return

    # Create two stacks
    s1 = []
    s2 = []

    # Push root to first stack
    s1.append(root)

    # Run while first stack is not empty
    while s1:

        # Pop an item from s1 and
        # append it to s2
        node = s1.pop()
        s2.append(node)

        # Push left and right children of
        # removed item to s1
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

        # Print all elements of second stack
    while s2:
        node = s2.pop()
        print(node.data, end=" ")


def inOrder(root):
    # Set current to root of binary tree
    current = root
    stack = []  # initialize stack

    while True:

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.left

        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif (stack):
            current = stack.pop()
            print(current.data, end=" ")  # Python 3 printing

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right

        else:
            break

    print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Post Order traversal of binary tree is")
postOrderIterative(root)
