from functools import cache
from pprint import pprint
class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        """
        :param matrix: 2D array of 0s and 1s
        :return: number of squares in the matrix that are all 1s
        """
        # idea is to use dynamic programming. 

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return 1 if matrix[0][0] == 0 else 0
        # dp[i][j] = size of the largest square that ends at (i, j) 
        count = 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            dp[i][0] = matrix[i][0]
            count += dp[i][0]
        for j in range(1, len(matrix[0])):
            dp[0][j] = matrix[0][j]
            count += dp[0][j]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    # if the current element is 1, then the number of squares that end at (i, j)
                    # is the minimum of the number of squares that end at (i-1, j), (i, j-1),
                    # and (i-1, j-1) plus 1.
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    count += dp[i][j]
        return count
# Time complexity: O(n*m), space: O(n*m)
print(Solution().countSquares([
  [1,0,1],
  [1,1,0],
  [1,1,0]
]))

        