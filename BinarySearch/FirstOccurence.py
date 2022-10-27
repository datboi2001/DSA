from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    """
    :param arr: list of integers
    :param target: the target to search for the first occurrence of
    :return: the index of the first occurrence of target in the list
    """
    left, right = 0, len(arr)
    first_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first_index = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return first_index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)