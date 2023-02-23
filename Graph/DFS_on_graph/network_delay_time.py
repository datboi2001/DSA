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
        
        # Main idea: Dijkstra's algorithm. The main idea is to use a priority queue to store the nodes that have not been visited.
        # The priority queue is sorted by the distance from the source node.
        # We pop the node with the smallest distance from the priority queue and add it to the dist dictionary.
        # Then, we add all the neighbors of the node to the priority queue.
        # We repeat the process until the priority queue is empty.
        # If the dist dictionary contains n nodes, then we return the maximum distance.
        pq = PriorityQueue()
        pq.put((0, k))
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # Dictionary that stores the distance from the source node to each node
        time = {}
        while not pq.empty():
            # Pop the node with the smallest distance
            d, node = pq.get()
            # If node has already been visited, continue
            if node in time:
                continue
            # Otherwise, add the distance to the dist dictionary
            else:
                time[node] = d
            # Add all the neighbors of the node to the priority queue
            for v, w in graph[node]:
                pq.put((d + w, v))
        return max(time.values()) if len(time) == n else -1

print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
