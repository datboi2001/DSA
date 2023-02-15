from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        seen = set()

        def dfs(node):
            if node in seen:
                return False
            if node == destination:
                return True
            seen.add(node)
            for neighbor in adj_list[node]:
                if dfs(neighbor):
                    return True
            return False
        
        return dfs(source)
