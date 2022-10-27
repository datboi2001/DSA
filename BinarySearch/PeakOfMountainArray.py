from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    """
    :param arr: list of integers with size >= 3
    :return: the index of the peak of the array
    """
    left, right = 0, len(arr) -1
    ans = None
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)
