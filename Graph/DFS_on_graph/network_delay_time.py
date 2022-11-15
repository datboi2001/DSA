from queue import PriorityQueue
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        :param times: list of edges with time
        :param n: number of nodes
        :param k: source node
        :return: the time it takes for all nodes to receive the signal or -1 if it is impossible
        """
        pq = PriorityQueue()
        pq.put((0, k))
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = {}
        while not pq.empty():
            # Pop the node with the smallest distance
            d, node = pq.get()
            # If node has already been visited, continue
            if node in dist:
                continue
            # Otherwise, add the distance to the dist dictionary
            else:
                dist[node] = d
            # Add all the neighbors of the node to the priority queue
            for v, w in graph[node]:
                pq.put((d + w, v))
        print(dist.values())
        return max(dist.values()) if len(dist) == n else -1

print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
