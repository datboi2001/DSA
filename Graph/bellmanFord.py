from collections import defaultdict


def bellmanFord(graph: dict[int, list[tuple[int, int]]], source: int, n: int) -> list[int]:
    """
    Given a directed graph, that can contain multiple edges and loops. Each edge has a weight that is expressed by a number (possibly negative). It is guaranteed that there are no cycles of negative weight.
    :param graph: adjacency list that represents a directed graph
    :param source: source node
    :param n: number of nodes
    :return: A list of distances from source to all nodes. If the path to the node is not found, the distance is set to 30000 
    """
    # Main idea: Bellman Ford algorithm. 
    # The algorithm is based on the idea that the shortest path from source to any node can have at most n-1 edges.
    # We start with the source node and relax all edges n-1 times.
    # If we relax an edge and the distance to the destination node is updated, we repeat the process.
    distance = [30000] * (n  + 1) 
    predecessor: list[int | None] = [None] * (n + 1) 
    distance[source] = 0

    # Relax all edges n-1 times
    for _ in range(n - 1):
        for node in graph:
            for neighbour, weight in graph[node]:
                if distance[node] + weight < distance[neighbour]:
                    distance[neighbour] = distance[node] + weight
                    predecessor[neighbour] = node
    return distance

n, m = [int(x) for x in input().split()] 
# Adjacency list
graph = defaultdict(list) 
for _ in range(m):
    from_node, to_node, weight = [int(x) for x in input().split()]
    graph[from_node].append((to_node, weight))

result = bellmanFord(graph, 1, n)
for i in range(1, n + 1):
    print(result[i], end=' ')
print()

