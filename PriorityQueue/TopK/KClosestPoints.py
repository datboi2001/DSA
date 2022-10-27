from typing import List
from heapq import heapify, heappop

def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    pq = []
    for pt in points:
        pq.append((pt[0] ** 2 + pt[1] ** 2, pt))
    heapify(pq)
    return [heappop(pq)[1] for _ in range(k)]

if __name__ == '__main__':
    points = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = k_closest_points(points, k)
    for row in res:
        print(' '.join(map(str, row)))