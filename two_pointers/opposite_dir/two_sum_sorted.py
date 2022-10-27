from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    i, j = 0, len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == target:
            return [i, j]
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum_sorted(arr, target)
    print(' '.join(map(str, res)))
