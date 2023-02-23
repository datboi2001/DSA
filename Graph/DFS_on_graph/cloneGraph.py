"""
# Definition for a Node.
"""
from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        :param node: the reference of a node in connected undirected graph
        :return: a deep copy of the graph
        Each node in the graph contains a value and a list of its neighbors
        """
        # Main idea: DFS. We do a DFS on the graph and create a new node for each node we visit. We keep track of the
        # nodes we have already visited in a dictionary. If we have already visited a node, we return the node
        # corresponding to that node from the dictionary. If we have not visited a node, we create a new node for
        # that node and add it to the dictionary. We also add the neighbors of the current node to the neighbors
        # list of the new node.

        # Time complexity: O(V + E) where V is the number of nodes and E is the number of edges
        # Space complexity: O(V) where V is the number of nodes
        if not node:
            return None
        if len(node.neighbors) == 0:
            return Node(node.val) 
        # Dictionary to keep track of the nodes we have already visited
        seen = {}
        # Do a DFS on the graph
        def dfs(node):
            # If we have already visited the node, return the node corresponding to that node from the dictionary
            if node in seen:
                return seen[node]
            # Create a new node for the current node
            new_node = Node(node.val)
            # Add the new node to the dictionary
            seen[node] = new_node
            for neighbor in node.neighbors:
                # Add the neighbors of the current node to the neighbors list of the new node
                new_node.neighbors.append(dfs(neighbor))
            # Return the new node
            return new_node
        return dfs(node)