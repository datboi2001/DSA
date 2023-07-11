
from collections import defaultdict
class Node:
    def __init__(self, city, time):
        self.city = city
        self.time = time

def minTime(roads: list[list[int]], machines: list[int]):
    """
    The kingdom of Zion has cities connected by bidirectional roads.
    There is a unique path between any pair of cities. Morpheus has found
    out that the machines are planning to destroy the whole kingdom.
    If two machines can join forces, they will attack. Neo has to destroy
    roads connecting cities with machines in order to stop them from joining forces. There must not be any path connecting two machines.
    Each of the roads takes an amount of time to destroy, 
    and only one can be worked on at a time.
    Given a list of edges and times, determine the minimum
    time to stop the attack.
    :param roads: 2d array of roads, each roads[i] = [city1, city2, time]
    :param machines: List of cities that contains the machines
    :return: minimum time to disrupt all the machine
    """
    # Main idea: 
    # 1. Build a graph from the roads
    # 2. Find the shortest path from each machine to all other machines
    # 3. Find the minimum time to disrupt all the machines
    graph = defaultdict(list)
    for city1, city2, time in roads:
        graph[city1].append(Node(city2, time))
        graph[city2].append(Node(city1, time)) 
    
    # Find the shortest path from each machine to all other machines
    # using Dijkstra's algorithm
    def dijkstra(start):
        # Initialize the distance from start to all other nodes
        dist = {node: float('inf') for node in graph}
        dist[start] = 0
        visited = set()
        while len(visited) < len(graph):
            # Find the node with the minimum distance
            min_node = None
            for node in graph:
                if node not in visited and (min_node is None or dist[node] < dist[min_node]):
                    min_node = node
            visited.add(min_node)
            for neighbor in graph[min_node]:
                dist[neighbor.city] = min(dist[neighbor.city], dist[min_node] + neighbor.time)
        return dist
    
    # Find the minimum time to disrupt all the machines
    # by finding the shortest path from each machine to all other machines

    # Initialize the minimum time to disrupt all the machines
    min_time = 0
    # Find the shortest path from each machine to all other machines
    for machine in machines:
        dist = dijkstra(machine)
        # Find the minimum time to disrupt all the machines
        for node in graph:
            if node != machine and node in machines:
                min_time += dist[node]
    return min_time

