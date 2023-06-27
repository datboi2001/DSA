from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1:
        return 0

    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Columns
    for c in range(n):
        if obstacleGrid[0][c] == 1:
            break
        dp[0][c] = 1
    # Rows
    for r in range(m):
        if obstacleGrid[r][0] == 1:
            break
        dp[r][0] = 1

    for r in range(1, m):
        for c in range(1, n):
            if obstacleGrid[r][c] == 1:
                dp[r][c] = 0
            else:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[-1][-1]


print(uniquePathsWithObstacles(
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
