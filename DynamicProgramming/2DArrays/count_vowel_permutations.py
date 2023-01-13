
"""
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

        Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
        Each vowel 'a' may only be followed by an 'e'.
        Each vowel 'e' may only be followed by an 'a' or an 'i'.
        Each vowel 'i' may not be followed by another 'i'.
        Each vowel 'o' may only be followed by an 'i' or a 'u'.
        Each vowel 'u' may only be followed by an 'a'.
        Since the answer may be too large, return it modulo 10^9 + 7.
        :param n: The length of the string
        :return: how many vowel strings of length n can be formed
        """
        # Idea: Dynamic Programming. We can use dynamic programming to solve this problem. The main
        # idea is that if we want to form a string of length n, we can use the vowels that are less than
        # or equal to n. So the number of vowel strings of length n is the sum of the following two cases:
        # 1. We use the vowel that is equal to n
        # 2. We use the vowel that is less than n and form a string of length n - 1

        dp = [[0] * 5 for _ in range(n + 1)]
        # dp[i][j] is the number of vowel strings of length i that end with vowel j
        # j = 0: 'a'
        # j = 1: 'e'
        # j = 2: 'i'
        # j = 3: 'o'
        # j = 4: 'u'
        for i in range(5):
            # Base case. There is only one way to form a string of length 1
            dp[1][i] = 1
        for i in range(2, n + 1):
            # Each vowel 'a' may only be followed by an 'e'.
            dp[i][0] = dp[i - 1][1]
            # Each vowel 'e' may only be followed by an 'a' or an 'i'.
            dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
            # Each vowel 'i' may not be followed by another 'i'.
            dp[i][2] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]
            # Each vowel 'o' may only be followed by an 'i' or a 'u'.
            dp[i][3] = dp[i - 1][2] + dp[i - 1][4]
            # Each vowel 'u' may only be followed by an 'a'.
            dp[i][4] = dp[i - 1][0]
        
        return sum(dp[n]) % (10 ** 9 + 7)
