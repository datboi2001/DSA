from typing import List

def find_min_rotated(arr: List[int]) -> int:
    """
    # Main idea: Binary search. The minimum element is the only element that is smaller than its right neighbor.
    :param arr: list of integers that were rotated at an unknown pivot
    :return: The index of the minimum element in this array
    """
    left, right = 0, len(arr)-1
    smallest_element = None
    while left <= right:
        mid = left + (right-left) // 2
        # If the mid element is the smallest element
        if arr[mid] < arr[mid-1]:
            smallest_element = arr[mid]
            break
        # If the mid element is the smallest element
        elif arr[mid] > arr[mid+1]:
            smallest_element = arr[mid+1]
            break
        # If the mid element is the smallest element
        elif arr[mid] > arr[right]:
            left = mid + 1
        # If the mid element is the smallest element
        else:
            right = mid - 1
    return smallest_element


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
