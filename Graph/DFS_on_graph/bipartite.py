class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        """
        :param graph: Two dimensional list where graph[u] is a list of nodes v
         such that (u, v) is an edge of the graph.
        :return: True if graph is bipartite, meaning it can be partition the nodes into two independent sets such that every edge
        connects a node in one and a node in the other.
        """
        if not graph:
            return True
        n = len(graph)
        # Color is a dictionary where color[u] is the color of node u.
        color = [0] * n
        for i in range(n):
            if color[i] == 0:
                color[i] = 1
                stack = [i]
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        # If neighbor is not colored, color it with the opposite color of node.
                        if color[neighbor] == 0:
                            color[neighbor] = -color[node]
                            stack.append(neighbor)
                        # If neighbor is colored with the same color as node, return False.
                        elif color[neighbor] == color[node]:
                            return False
        return True

# Time complexity: O(V+E), where V is the number of nodes and E is the number of edges.
# Space complexity: O(V), where V is the number of nodes.