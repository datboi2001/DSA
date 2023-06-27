import math
class TreeAncestor:

    def __init__(self, n: int, parent: list[int]):
        """
        :param n: The number of nodes in the tree.
        :param parent: parent[i] is the parent of node i. parent[0] = -1.
        """
        # Main idea: Dynamic programming. Store the 2^i-th ancestor of each node.
        # For example, if we want to find the 8-th ancestor of node 5, we can find the 4-th ancestor of node 5,
        # and then find the 4-th ancestor of the 4-th ancestor of node 5.
        # The 4-th ancestor of the 4-th ancestor of node 5 is the 8-th ancestor of node 5.
        # We can use binary search to find the 4-th ancestor of node 5. 
        
        # The number of ancestors of each node is log(n).
        self.ancestors = [[-1] * n for _ in range(int(math.log2(n)) + 1)]
        # ancestors is a 2D array. ancestors[i][j] is the 2^i-th ancestor of node j.
        self.ancestors[0] = parent

        # Fill the ancestors array.
        for i in range(1, len(self.ancestors)):
            for j in range(n):
                if self.ancestors[i - 1][j] != -1:
                    # The 2^i-th ancestor of node j is the 2^(i-1)-th ancestor of the 2^(i-1)-th ancestor of node j.
                    self.ancestors[i][j] = self.ancestors[i - 1][self.ancestors[i - 1][j]]
        

    def getKthAncestor(self, node: int, k: int) -> int:
        """
        :param node: The index of the node.
        :param k: The number of ancestors to find.
        """

        # Main idea: Binary search. Find the 2^i-th ancestor of node. If k is greater than 2^i, then we can find
        # the 2^(i+1)-th ancestor of node. If k is less than 2^i, then we can find the 2^(i-1)-th ancestor of node.

        # Find the 2^i-th ancestor of node.
        for i in range(len(self.ancestors) - 1, -1, -1):
            if k >= 2 ** i:
                node = self.ancestors[i][node]
                k -= 2 ** i
            if node == -1:
                return -1
        return node