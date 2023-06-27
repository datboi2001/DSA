from typing import List
from collections import Counter

def subarray_sum(arr: List[int], target: int) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    prefix_sum = {0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        difference = cur_sum - target
        if difference in prefix_sum:
            return [prefix_sum[difference], i + 1]
        prefix_sum[cur_sum] = i + 1


def subarray_sum_total(arr: List[int], target: int) -> int:
    # Find all subarrays that sum up to target
    prefix_sum = Counter({0: 1})
    cur_sum = 0
    count = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        difference = cur_sum - target
        if difference in prefix_sum:
            count += prefix_sum[difference]
        prefix_sum[cur_sum] += 1
    return count

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum(arr, target)
    print(' '.join(map(str, res)))
