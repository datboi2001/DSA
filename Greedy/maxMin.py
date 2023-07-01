import sys
def maxMin(k, arr):
    """
    Given an array of integers, find the minimum possible unfairness
    after selecting k elements from the array.
    :param k: the number of elements to select
    :param arr: an array of integers
    :return: the minimum possible unfairness
    """
    # Main idea: sort the array and then compare the difference between
    # the smallest and largest elements in each subarray of length k.
    # This idea works because the difference between the smallest and
    # largest elements in each subarray of length k is the unfairness
    # of that subarray.