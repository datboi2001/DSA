class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        """
        :param text1: a string
        :param text2: a string
        :return: the length of their longest common substring
        """
        # Idea: Dynamic Programming. We can use dynamic programming to solve this problem. The main
        # idea is that if we want to find the longest common substring of two strings, we can use
        # the characters that are less than or equal to the current characters. So the length of the
        # longest common substring of two strings is the maximum of the following two cases:
        # 1. We use the character that is equal to the current characters
        # 2. We use the character that is less than the current characters and find the longest common
        # substring of the remaining strings

        # dp[i][j] is the length of the longest common substring of text1[:i] and text2[:j]
        # We need an extra row and an extra column to handle the case when the string is empty
        dp = [[0 for _ in range(len(text2) + 1 )] for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                # If the current characters are equal, we can use them to find the longest common
                if text1[i-1] == text2[j-1]:
                    # If the current characters are equal, we can use them to find the longest common
                    # substring of the remaining strings
                    dp[i][j] = 1 + dp[i-1][j-1]

        # The longest common substring is the maximum of the values in the last row
        return max(max(row) for row in dp)