class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        """
        You are given an initial computer network connections.
        You can extract certain cables between two directly connected computers,
        and place them between any pair of disconnected computers to make them
        directly connected.
        :param connections: list of connections
        :param n: number of computers
        :return: Minimum number of times you need to do this in order to make
        all the computers connected.
        """
        if not connections:
            return -1
        if len(connections) < n - 1:
            return -1
        roots = [-1] * n

        def find(x):
            if roots[x] < 0:
                return x
            else:
                res = find(roots[x])
                roots[x] = res
                return res
        
        def union(i, j):
            ri = find(i)
            rj = find(j)
            size1 = roots[ri] * -1
            size2 = roots[rj] * -1
            if size1 < size2:
                roots[ri] = rj
                roots[rj] = (size1 + size2) * -1
            else:
                roots[rj] = ri
                roots[ri] = (size1 + size2) * -1
        
        for i, j in connections:
            if find(i) != find(j):
                union(i, j)
        return len([root for root in roots if root < 0]) - 1


print(Solution().makeConnected(4, [[0,1],[0,2],[1,2]]))