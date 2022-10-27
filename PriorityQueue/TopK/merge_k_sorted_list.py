from heapq import heapify, heappop, heappush
from typing import List
def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    heap = []
    for cur_list in lists:
        heappush(heap, (cur_list[0], cur_list, 0))
    while len(heap) > 0:
        val, current_list, head_index = heappop(heap)
        res.append(val)
        head_index += 1

        if head_index < len(current_list):
            heappush(heap, (current_list[head_index], current_list, head_index))
    return res


if __name__ == '__main__':
    lists = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_k_sorted_lists(lists)
    print(' '.join(map(str, res)))
