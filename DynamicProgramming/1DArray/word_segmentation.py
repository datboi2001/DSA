def word_segmentation(s, quality) -> str:
    """
    :param s: the string to segment
    :param quality: a function that takes in a string and returns the quality of that string
    :return: the optimal segmentation of s
    """
    # Main idea: We can use dynamic programming to solve this problem. Let dp[i] be the maximum quality we can
    # achieve by segmenting the first i characters of s. Then, we can calculate dp[i] as follows:
    # dp[i] = max(dp[i], dp[j] + quality(s[j:i])) where j < i
    # The base case is dp[0] = 0
    # As we calculate the maximum total quality, we can also keep track of the optimal segmentation of s in a
    # separate array. This array will be called optimal. optimal[i] will be the optimal segmentation of the first
    # i characters of s. Then, we can calculate optimal[i] as follows:
    # optimal[i] = optimal[j] + [s[j:i]] where j < i and dp[i] = dp[j] + quality(s[j:i])

    # In the end we join the optimal segmentation of s with spaces in between each word
    n = len(s)
    dp: list[None | int] = [None] * (n+1)
    dp[0] = 0
    optimal: list[list[str]] = [[] for _ in range(n+1)]
    optimal[0] = []
    # Loop through all possible segmentations of s
    for i in range(1, n+1):
        max_quality = float('-inf')
        for j in range(i):
            current_quality = quality(s[j:i])
            # If the current quality is greater than the maximum quality, update the maximum quality and the
            # optimal segmentation of s
            if dp[j] is not None and current_quality + dp[j] > max_quality:
                max_quality = current_quality + dp[j]
                dp[i] = max_quality
                optimal[i] = optimal[j] + [s[j:i]]
    return " ".join(optimal[n])