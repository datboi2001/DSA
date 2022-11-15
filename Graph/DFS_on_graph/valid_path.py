from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        """
        :param n: number of nodes
        :param edges: list of edges 
        :param source: source node
        :param destination: destination node
        :return: True if there is a path from source to destination, False otherwise
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(graph[node])
        return False
    
