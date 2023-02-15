class Solution:


    def isBipartite(self, graph: list[list[int]]) -> bool:
        """
        :param graph: Two dimensional list where graph[u] is a list of nodes v
         such that (u, v) is an edge of the graph.
        :return: True if graph is bipartite, meaning it can be partition the nodes into two independent sets such that every edge
        connects a node in one and a node in the other.
        """
        # Idea: Use DFS to traverse the graph. If we find a node that has been visited before, then we check if the color of the
        # node is the same as the color of the current node. If so, then the graph is not bipartite. Otherwise, we continue
        # traversing the graph.
        # Time complexity: O(V + E), where V is the number of nodes and E is the number of edges.
        # Space complexity: O(V), where V is the number of nodes.

        # Initialize the color of each node to be -1.
        
        def dfs(color, node, c):
            """
            :param color: List of colors of each node.
            :param node: The current node.
            :param c: The color of the current node.
            """

            color[node] = c
            for neighbor in graph[node]:
                # If the neighbor has not been visited, then we traverse the graph starting from this neighbor.
                if color[neighbor] == -1:
                    if not dfs(color, neighbor, 1 - c):
                        return False
                # If the neighbor has been visited, then we check if the color of the neighbor is the same as the color of the
                # current node.
                elif color[neighbor] == c:
                    return False
            return True

        color = [-1] * len(graph)
        # Traverse the graph.
        for i in range(len(graph)):
            # If the node has not been visited, then we traverse the graph starting from this node.
            if color[i] == -1:
                # If the graph is not bipartite, then return False.
                if not dfs(color, i, 0):
                    return False
        # If the graph is bipartite, then return True.
        return True


print(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]));
