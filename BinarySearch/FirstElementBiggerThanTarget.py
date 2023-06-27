from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    """
    :param arr: list of integers
    :param target: An integer to compare against
    :return: the index of the first element in
    the array that is larger than or equal to the target
    """
    left, right = 0, len(arr) - 1
    first_index = None
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            first_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return first_index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)
