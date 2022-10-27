from typing import List
from collections import deque

def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    queue = deque([a])
    visited = set(a)
    step = 0
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if node == b:
                return step
            for child in graph[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
        step += 1


if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)
