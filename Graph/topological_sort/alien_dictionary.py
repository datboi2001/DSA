from typing import List
from heapq import heappop, heappush

def count_parents(graph):
    counts = {node: 0 for node in graph}
    for _, nodes in graph.items():
        for node in nodes:
            counts[node] += 1
    return counts


def topo_sort(graph):
    res = []
    pqueue = []
    counts = count_parents(graph)
    for node in counts:
        if counts[node] == 0:
            heappush(pqueue, node)

    while len(pqueue) > 0:
        node = heappop(pqueue)
        res.append(node)
        for child in graph[node]:
            counts[child] -= 1
            if counts[child] == 0:
                heappush(pqueue, child)

    for count in counts.values():
        if count != 0:
            return ""
    return "".join(res)


def alien_order(words: List[str]) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    graph = {c: set() for word in words for c in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                break
    return topo_sort(graph)



if __name__ == '__main__':
    words = input().split()
    res = alien_order(words)
    print(res)
