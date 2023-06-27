from typing import List
from heapq import heapify, heappop
def find_kth_largest(nums: List[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    heap = [-x for x in nums]
    heapify(heap)
    result = None
    for _ in range(k):
        result = heappop(heap)
    return result * -1

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = find_kth_largest(nums, k)
    print(res)
