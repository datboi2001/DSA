from collections import deque
from typing import List, Tuple

def shortest_path(graph: List[List[Tuple[int, int]]], a: int, b: int) -> int:
    def get_neighbors(node: int):
        return graph[node]

    def bfs(root: int, target: int):
        queue = deque([root])
        distance = [float('inf')] * len(graph)
        distance[root] = 0
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor, weight in get_neighbors(node):
                if distance[neighbor] <= distance[node] + weight:
                    continue
                queue.append(neighbor)
                distance[neighbor] = distance[node] + weight
        return distance[target]

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
