import sys
def minimumAbsoluteDifference(arr):
    """
    Given an array of integers, find and print the minimum absolute
    difference between any two elements in the array.
    :param: 1d array of integers
    :return: the minimum absolute difference found
    """
    # Write your code here
    min_abs = sys.maxsize

    # Main idea: sort the array and then compare adjacent elements.
    # This idea works because the absolute difference between any two
    # elements in the array is minimized when the two elements are
    # adjacent to each other.
    arr.sort()
    for i in range(len(arr)-1):
        cur_diff = abs(arr[i] - arr[i+1])
        min_abs = min(min_abs, cur_diff)
    return min_abs

print(minimumAbsoluteDifference([3,-7,0]))