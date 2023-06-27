class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :param s: string
        :return: longest palindrome substring
        """
        # Main idea: Dynamic Programming. The main idea is to maintain a table
        #  dp[i][j] which is true if s[i:j] is a palindrome, otherwise false.
        # Then the state transition function is:
        # dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        # Base case: dp[i][i] = True
        #           dp[i][i+1] = (s[i] == s[i+1])
        # Recurrence relation: dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        # Time complexity: O(n^2)
        # Space complexity: O(n^2)
        if not s:
            return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        # Max length of palindrome
        max_len = 1
        # Start index of palindrome
        start = 0
        # Loop through all substrings
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # If the first and last characters match
                if s[i] == s[j]:
                    # If the length of substring is 2 or 3, then it is a palindrome
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        # Update max length and start index
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            start = i
        return s[start:start+max_len]
print(Solution().longestPalindrome("cbbd"))