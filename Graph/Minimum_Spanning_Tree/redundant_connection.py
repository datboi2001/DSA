class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """
        You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
        :param edges: list of edges
        :return: list of two integers that represent the edge that can be removed
        """

        # Main idea: use union find to find the cycle in the graph. If there is a cycle, then the edge that forms the cycle
        # is the redundant edge.

        # Initialize the union find data structure
        roots = [-1] * len(edges)
        def find(n):
            if roots[n] < 0:
                return n
            else:
                res = find(roots[n])
                roots[n] = res
                return res
        
        def union(i, j):
            ri = find(i)
            rj = find(j)
            size1 = roots[ri] * -1
            size2 = roots[rj] * -1
            if size1 < size2:
                # bring ri into rj
                roots[ri] = rj
                roots[rj] = (size1 + size2) * -1
            else:
                roots[rj] = ri
                roots[ri] = (size1 + size2) * -1
        
        # Iterate through the edges
        for start, to in edges:
            if find(start - 1) != find(to -1):
                union(start - 1, to - 1)
            else:
                return [start, to]