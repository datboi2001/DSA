from pprint import pprint
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        """
        Given a two dimensional array, return the length of the longest increasing path.
        :param matrix: Two dimensional arra
        :return: The length of the longest increasing path
        """
        def dfs(i: int, j: int) -> int:
            """
                Perform DFS algorithm to find the longest increasing path starting at (i, j)
            """
            if dp[i][j] != 0:
                return dp[i][j]
            directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for x, y in directions:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    # If the next cell is larger than the current cell, then we can go to the next cell
                    dp[i][j] = max(dp[i][j], dfs(x, y))
            # Add 1 to the current cell
            dp[i][j] += 1
            return dp[i][j]


        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        # dp[i][j] = longest increasing path starting at (i, j)
        dp = [[0] * n for _ in range(m)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j] = dfs(i, j)
        pprint(dp)
        return max([max(row) for row in dp])
    # Time complexity: O(mn) where m is the number of rows and n is the number of columns
    # Space complexity: O(mn) where m is the number of rows and n is the number of columns

print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))