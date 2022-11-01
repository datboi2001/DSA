

def longest_good_subsequence(arr: list[int]):
    """
    For this problem, we define a bad pair as two elements of an array, 
    i < j where a[j] -a[i] < j - i.
    We define a good subsequence as a subset of elements of a such that there
    are no bad pairs between any two elements using the indices of the element
    from the original array for i and j.

    What is the longest good subsequence in the given array?
    :param arr: Array
    :return: Length of longest good subsequence
    """
    # Initialize the dp array
    dp = [1 for _ in range(len(arr))]
    # Iterate through the array
    for i in range(1, len(arr)):
        # Iterate through the array again
        for j in range(i):
            # If the current element is greater than the previous element
            # and the difference between the indices is greater than the difference
            # between the elements, then we can add the current element to the
            # previous element's subsequence
            if not (arr[i] - arr[j] < i - j):
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
# Time complexity: O(n^2)
# Space complexity: O(n)

n = int(input())
arr = [int(x) for x in input().split()]
print(longest_good_subsequence(arr))