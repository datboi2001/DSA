from typing import List
from heapq import heappop, heappush, heapify

def kth_smallest(matrix: List[List[int]], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if not matrix or k < 1:
        return
    s = set()
    s.add((0, 0))
    heap = [(matrix[0][0], 0, 0)]
    while k > 1:
        val, row, col = heappop(heap)
        if col + 1 < len(matrix[0]) and (row, col + 1) not in s:
            heappush(heap, (matrix[row][col+1], row, col +1))
            s.add((row, col + 1))
        if row + 1 < len(matrix) and (row + 1, col) not in s:
            heappush(heap, (matrix[row + 1][col], row + 1, col))
            s.add((row + 1, col))
        k -= 1
    return heap[0][0]

if __name__ == '__main__':
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = kth_smallest(matrix, k)
    print(res)
