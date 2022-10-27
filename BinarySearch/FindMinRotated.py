from typing import List

def find_min_rotated(arr: List[int]) -> int:
    """
    :param arr: list of integers that were rotated at an unknown pivot
    :return: The index of the minimum element in this array
    """
    left, right = 0, len(arr)-1
    smallest_element = None
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
            smallest_element = mid
            right = mid - 1
        else:
            left = mid + 1
    return smallest_element

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
