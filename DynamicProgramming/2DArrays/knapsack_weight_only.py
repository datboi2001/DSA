from typing import List


def knapsack_weight_only(weights: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(weights)
    total_sum = sum(weights)
    dp = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for w in range(0, total_sum + 1):
            dp[i][w] = dp[i][w] or dp[i - 1][w]
            if w - weights[i - 1] >= 0:
                dp[i][w] = dp[i][w] or dp[i - 1][w - weights[i - 1]]
    ans = []
    for w in range(0, total_sum + 1):
        if dp[n][w]:
            ans.append(w)
    return ans


if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    res = knapsack_weight_only(weights)
    res.sort()
    for i in range(len(res)):
        print(res[i], end='')
        if i != len(res) - 1:
            print(' ', end='')
    print()
