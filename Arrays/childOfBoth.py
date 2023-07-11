def commonChild(s1, s2):
    """
    # Find the length of the longest string which is a common child of the input strings.
    :param s1: string
    :param s2: string
    :return: int
    """
    # Write your code here
    # Main idea: Dynamic programming. Let dp[i][j] be the length of the longest
    # common child of s1[:i] and s2[:j].
    #  If s1[i] == s2[j], then dp[i][j] = dp[i-1][j-1] + 1 because we can add
    # s1[i] to the longest common child of s1[:i-1] and s2[:j-1]. 

    # If s1[i] != s2[j], then dp[i][j] = max(dp[i-1][j], dp[i][j-1]) because
    # we can add s1[i] to the longest common child of s1[:i-1] and s2[:j] or
    # we can add s2[j] to the longest common child of s1[:i] and s2[:j-1].

    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(s1)][len(s2)]
    

print(commonChild('HARRY', 'SALLY'))