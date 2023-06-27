from typing import List, Dict
from collections import defaultdict, deque


def count_parents(graph: Dict[str, List[str]]):
    counts = {node: 0 for node in graph}
    for _, nodes in graph.items():
        for node in nodes:
            counts[node] += 1
    return counts


def topo_sort(graph: Dict[str, List[str]], task_times: Dict[str, int]):
    ans = 0
    queue = deque()
    dis = defaultdict(int)
    counts = count_parents(graph)
    for node, parent_count in counts.items():
        if parent_count == 0:
            queue.append(node)
            dis[node] = task_times[node]
            ans = max(ans, dis[node])

    while len(queue) > 0:
        node = queue.popleft()
        for child in graph[node]:
            counts[child] -= 1
            dis[child] = max(dis[child], dis[node] + task_times[child])
            ans = max(ans, dis[child])
            if counts[child] == 0:
                queue.append(child)
    return ans


def task_scheduling_2(tasks: List[str], times: List[int], requirements: List[List[str]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    graph = {}
    task_times = {}
    for i in range(len(tasks)):
        graph[tasks[i]] = []
        task_times[tasks[i]] = times[i]

    for req in requirements:
        graph[req[0]].append(req[1])
    return topo_sort(graph, task_times)


if __name__ == '__main__':
    tasks = input().split()
    times = [int(x) for x in input().split()]
    requirements = [input().split() for _ in range(int(input()))]
    res = task_scheduling_2(tasks, times, requirements)
    print(res)
