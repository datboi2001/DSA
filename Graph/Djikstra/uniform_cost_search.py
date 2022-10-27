from heapq import heappop, heappush
from typing import List, Tuple

def shortest_path(graph: List[List[Tuple[int, int]]], a: int, b: int) -> int:
    def get_neighbors(node: int):
        return graph[node]

    def bfs(root: int, target: int):
        queue = [(0, root)]
        distances = [float('inf')] * len(graph)
        distances[root] = 0
        while len(queue) > 0:
            distance, node = heappop(queue)
            if node == target:
                return distance
            if distance > distances[node]:
                continue
            for neighbor, weight in get_neighbors(node):
                d = distances[node] + weight
                if distances[neighbor] <= d:
                    continue
                heappush(queue, (d, neighbor))
                distances[neighbor] = d
        return distances[target]

    return -1 if bfs(a, b) == float('inf') else bfs(a, b)

if __name__ == '__main__':
    graph = []
    for _ in range(int(input())):
        s = input().split()
        neighbours = []
        for i in range(0, len(s), 2):
            neighbours.append((int(s[i]), int(s[i+1])))
        graph.append(neighbours)
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)
