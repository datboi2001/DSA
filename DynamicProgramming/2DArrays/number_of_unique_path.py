def unique_paths(m: int, n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1,m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    res = unique_paths(m, n)
    print(res)
