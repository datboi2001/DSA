from typing import List, Tuple

from heapq import heappush, heappop

def shortest_path(graph: List[List[Tuple[int, int]]], a: int, b: int) -> int:
    def get_neighbors(node: int):
        return graph[node]

    def bfs(root: int, target: int):
        queue = [(0, root)]
        distances = []
        for i in range(len(graph)):
            if i == root:
                distances.append(0)
                heappush(queue, (0, i))
            else:
                distances.append(float('inf'))
                heappush(queue, (float('inf'), i))
        while len(queue) > 0:
            _, node = heappop(queue)
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
