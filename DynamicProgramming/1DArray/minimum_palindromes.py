from sys import maxsize
class Solution:
    def minCut(self, s: str) -> int:
        """
        Given a string s, partition s such that every 
        substring of the partition is a palindrome.
        Return the minimum cuts needed for a palindrome partitioning of s.
        :param s: string
        :return: minimum cuts needed for a palindrome partitioning of s
        """
        # Main idea: Dynamic Programming. The main idea is to maintain a table
        #  dp[i][j] which is true if s[i:j] is a palindrome, otherwise false.
        # Then the state transition function is:
        # dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        # Base case: dp[i][i] = True
        #           dp[i][i+1] = (s[i] == s[i+1])
        # Recurrence relation: dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        # Create another table min_cuts[i] which is the minimum cuts needed for
        #  a palindrome partitioning of s[:i]
        # min_cuts[i] = min(min_cuts[i], min_cuts[j] + 1) for all j < i
        # Time complexity: O(n^2)
        # Space complexity: O(n^2)
        if not s:
            return 0
        n = len(s) 
        dp = [[False] * n for _ in range(n)]

        # dp[i][j] is true if s[i:j] is a palindrome
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # Check if s[i:j] is a palindrome
                if s[i] == s[j]:
                    # Check if s[i+1:j-1] is a palindrome
                    if j - i == 1 or dp[i+1][j-1]:
                        # Update dp[i][j]
                        dp[i][j] = True
        # min_cuts[i] is the minimum cuts needed for a palindrome partitioning of s[:i]
        min_cuts : list[int] = [-maxsize] * (n+1)
        # Base case: min_cuts[0] = -1 because s[:0] is an empty string
        min_cuts[0] = -1
        for i in range(1, n+1):
            for j in range(i):
                # Check if s[j:i] is a palindrome
                if dp[j][i-1]:
                    # Update the minimum cuts needed for a palindrome partitioning of s[:i]
                    min_cuts[i] = min(min_cuts[i], min_cuts[j] + 1)
        return min_cuts[n]