# 3.You are given a dataset containing both integers and strings.
# Design a sorting algorithm that can handle this mixed dataset.
# The sorting should be such that integers are sorted first in ascending order,
# followed by strings sorted in alphabetical order.

# Example input: [4, 1, 8, 9, 2, 'k', 'a', 'd', 'h', 'b', 'z']
# Example output: [1, 2, 4, 8, 9, 'a', 'b', 'd', 'h', 'k', 'z']

# Solution: We can use the merge sort algorithm to solve this problem.
# The merge sort algorithm is a divide and conquer algorithm.

# The merge sort algorithm works as follows:
# 1. Divide the unsorted list into n sublists, each containing 1 element
# (a list of 1 element is considered sorted).
# 2. Repeatedly merge sublists to produce new sorted sublists until there is
# only 1 sublist remaining. This will be the sorted list.

import random
import string





def mixed_merge_sort(lst: list[int | str]) -> list[int | str]:
    """
    :param lst: list of integers and strings
    :return: sorted list of integers and strings
    """
    # base case
    if len(lst) <= 1:
        return lst
    # recursive case
    # split the list into two halves
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    # recursively sort each half
    mixed_merge_sort(left)
    mixed_merge_sort(right)
    # merge the sorted halves

    # create two pointers for the left and right sublists
    l = 0
    r = 0
    k = 0
    while l < len(left) and r < len(right):
        # if the left element is an integer and the right element is a string
        if type(left[l]) is int and type(right[r]) is str:
            # append the left element to the merged list
            lst[k] = left[l]
            # increment the left pointer
            l += 1
        # if the left element is a string and the right element is an integer
        elif type(left[l]) is str and type(right[r]) is int:
            # append the right element to the merged list
            lst[k] = right[r]
            # increment the right pointer
            r += 1
        # If both elements are integers or both elements are strings
        else:
            if left[l] < right[r]:
                # append the left element to the merged list
                lst[k] = left[l]
                # increment the left pointer
                l += 1
            else:
                # append the right element to the merged list
                lst[k] = right[r]
                # increment the right pointer
                r += 1
        # increment the merged list pointer
        k += 1
    # if there are any remaining elements in the left sublist
    while l < len(left):
        # append the left element to the merged list
        lst[k] = left[l]
        # increment the left pointer
        l += 1
        k += 1
    # if there are any remaining elements in the right sublist
    while r < len(right):
        # append the right element to the merged list
        lst[k] = right[r]
        # increment the right pointer
        r += 1
        k += 1
    # return the merged list
    return lst
# Time Complexity: Worst-case: O(nlogn) Best-case: O(nlogn)
# Space Complexity: O(n) since we are creating new lists for each recursive call

lst = []
# Create a list of integers and strings
for i in range(100):
    # Flip a coin, if it's heads, add a random integer to the list
    if random.randint(0, 1) == 0:
        lst.append(random.randint(0, 1000))
    else:
        # Otherwise, add a random string to the list
        lst.append(''.join(random.choices(string.ascii_lowercase, k=5))) 


print(lst)
print(mixed_merge_sort(lst))