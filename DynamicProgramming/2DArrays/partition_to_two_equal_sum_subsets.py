from typing import List

def can_partition(nums: List[int]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    nums.sort(reverse=True)
    n = len(nums)
    dp = [[False for _ in range(target + 1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        for s in range(target +1):
            if s < nums[i-1]:
                dp[i][s] = dp[i-1][s]
            else:
                dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
    return dp[n][target]

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = can_partition(nums)
    print('true' if res else 'false')
