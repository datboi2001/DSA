class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        :param points: list of points
        :return: minimum cost to connect all points
        """
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        edges.sort(key=lambda x: x[2])
        roots = [-1] * len(points)
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
                roots[ri] = rj
                roots[rj] = (size1 + size2) * -1
            else:
                roots[rj] = ri
                roots[ri] = (size1 + size2) * -1
        res = 0
        for start, to, weight in edges:
            if find(start) != find(to):
                union(start, to)
                res += weight
        return res

print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))