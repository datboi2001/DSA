from heapq import heappop, heappush
from typing import List
def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    heap = []
    for cur_list in lists:
        # Push the first element of each list into the heap
        heappush(heap, (cur_list[0], cur_list, 0))
    while len(heap) > 0:
        # Pop the smallest element from the heap
        val, current_list, head_index = heappop(heap)
        # Add the smallest element to the result list
        res.append(val)
        head_index += 1

        if head_index < len(current_list):
            # Push the next element of the list into the heap
            heappush(heap, (current_list[head_index], current_list, head_index))
    return res


if __name__ == '__main__':
    lists = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_k_sorted_lists(lists)
    print(' '.join(map(str, res)))
