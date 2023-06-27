
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        """
        :param routes: an array representing bus routes where routes[i] is a bus route that the ith bus repeats forever
        :param source: the source bus stop
        :param target: the target bus stop
        :return: the least number of buses we must take to reach our destination. Return -1 if it is not possible
        """
        # Idea: BFS. We can think of the problem as a graph problem. Each bus route is a node and there is an edge between
        # two bus routes if they share at least one bus stop. The problem is to find the shortest path from the source to
        # the target. We can use BFS to find the shortest path.


        # Step 1: build the graph

        graph = defaultdict(list) 
        for i in range(len(routes)):
            for stop in routes[i]:
                graph[stop].append(i)
        
        # Step 2: BFS

        visited = set()
        # Queue stores the bus stop and the number of buses we have taken so far
        queue = deque[tuple[int, int]]([(source, 0)])

        while queue:
            stop, num_buses = queue.popleft()
            # If we have reached the target, return the number of buses we have taken so far
            if stop == target:
                return num_buses
            # Otherwise, add the buses that can take us to the next stop to the queue
            for bus in graph[stop]:
                # If we have not visited the bus, add it to the queue
                if bus not in visited:
                    visited.add(bus)
                    # Add the next stop and the number of buses we have taken so far to the queue
                    for next_stop in routes[bus]: 
                        queue.append((next_stop, num_buses + 1))
        return -1

print(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))

