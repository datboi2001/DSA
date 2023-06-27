def candies(n, arr):
    # Write your code here
    """
    :param n: Number of children
    :param arr: list of ratings
    :return: Minimum number of candies
    """
    dp = [1 for _ in range(n)]
    # Iterate through the array
    for i in range(1, n):
        # If the current rating is greater than the previous,
        # then we can give the current child one more candy than the previous
        if arr[i] > arr[i - 1]:
            dp[i] = dp[i - 1] + 1
    # Iterate through the array backwards
    for i in range(n-2, -1, -1):
        # If the current rating is greater than the next,
        # then we can give the current child one more candy than the next
        if arr[i] > arr[i + 1]:
            dp[i] = max(dp[i], dp[i + 1] + 1)
    return sum(dp)
