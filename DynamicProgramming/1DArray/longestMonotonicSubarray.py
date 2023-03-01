def longest_monotonic_increasing(a: list[int]) -> list[int]:
    """
    :param a: a list of integers
    :return: the longest increasing monotonic subarray of a. 
    """
    # Main idea: Two pointers. 
    if not a:
        return []
    n = len(a)
    longest = [a[0]]
    curr = [a[0]]
    for i in range(1, n):
        if a[i] <= a[i - 1]:
            curr.append(a[i])
        else:
            if len(curr) > len(longest):
                longest = curr
            curr = [a[i]]
    if len(curr) > len(longest):
        longest = curr
    return longest

print(longest_monotonic_increasing([1, 2, 8]))