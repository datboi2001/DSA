class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        :param triangle: two dimensional list that represents a triangle
        :return: Minimum path sum from top to bottom
        """
        if not triangle:
            return 0
        # Initialize the dp array
        dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
        # Set the first element to the first element in the triangle
        dp[0][0] = triangle[0][0]
        # Iterate through the triangle
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                # If we are at the first element, then we can only go down
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                # If we are at the last element, then we can only go down
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                # Otherwise, we can go down or diagonally
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[-1])