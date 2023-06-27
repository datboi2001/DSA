from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        :param text1: a string
        :param text2: a string
        :return:  the length of their longest common subsequence
        """ 
        # Idea: Dynamic Programming. We can use dynamic programming to solve this problem. The main
        # idea is that if we want to find the longest common subsequence of two strings, we can use
        # the characters that are less than or equal to the current characters. So the length of the
        # longest common subsequence of two strings is the maximum of the following two cases:
        # 1. We use the character that is equal to the current characters
        # 2. We use the character that is less than the current characters and find the longest common
        # subsequence of the remaining strings

        @cache
        def common_subsequence_recursion(i: int, j: int) -> int:
            """
            :param i: the index of the first string
            :param j: the index of the second string
            :return: the length of their longest common subsequence
            """
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return 1 + common_subsequence_recursion(i - 1, j - 1)
            return max(common_subsequence_recursion(i - 1, j), common_subsequence_recursion(i, j - 1))

        def common_subsequence_dp():
            # dp[i][j] is the length of the longest common subsequence of text1[:i] and text2[:j]
            dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
            for i in range(1, len(text1) + 1):
                for j in range(1, len(text2) + 1):
                    if text1[i - 1] == text2[j - 1]:
                        # If the current characters are equal, we can use them to find the longest common
                        # subsequence of the remaining strings
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        # If the current characters are not equal, we can use the characters that are less
                        # than the current characters to find the longest common subsequence of the remaining
                        # strings
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp[-1][-1]

        return common_subsequence_recursion(len(text1) - 1, len(text2) -1)