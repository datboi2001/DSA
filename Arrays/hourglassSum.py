import sys
def hourglassSum(arr: list[list[int]]):
    """
    An hourglass A is a subset of values with indices falling in this pattern in arr's graphical representation:
    a b c
      d
    e f g
    :param arr: a 6x6 array
    :return: the maximum hourglass sum in the array
    """
    # Write your code here
    max_sum: int = -sys.maxsize
    # How to find hour glassses:
    # 1. Start from the top left corner of the array
    # 2. Move right 2 times
    # 3. Move down 1 time
    # 4. Move left 2 times


    # We can only move right 4 times
    for i in range(4):
        for j in range(4):
            current_sum: int = 0
            current_sum += arr[i][j] + arr[i][j+1] + arr[i][j+2]
            current_sum += arr[i+1][j+1]
            current_sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            max_sum = max(max_sum, current_sum)
    return max_sum
