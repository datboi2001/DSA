# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    """
    Given an array without any duplicates, you are allowed to swap
    any two elements. Find the minimum number of swaps required to
    sort the array in ascending order.
    :param: 1d array of integers
    :return: the minimum number of swaps required to sort the array
    """
    i = 0
    swap = 0

    while i < len(arr):
        cur_elem = arr[i]
        if cur_elem != i+1:
            # Swap the current element with the element at the correct position
            arr[i], arr[cur_elem-1] = arr[cur_elem-1], arr[i]
            swap += 1
        else:
            i += 1
    return swap


if __name__ == "__main__":
    print(minimumSwaps([7,1,3,2,4,5,6]))
