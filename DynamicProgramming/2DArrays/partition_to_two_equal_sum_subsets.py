from typing import List

def can_partition(nums: List[int]) -> bool:
    """
    :param nums: a list of integers
    :return: True if we can partition nums into two subsets with equal sum
    """
    # WRITE YOUR BRILLIANT CODE HERE
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    nums.sort(reverse=True)
    n = len(nums)
    # dp[i][s] = True if we can get sum s from first i elements
    dp = [[False for _ in range(target + 1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):
        for s in range(target +1):
            if s < nums[i-1]:
                # if the current element is greater than the sum, we can't include it
                dp[i][s] = dp[i-1][s]
            else:
                # else we can include it or exclude it
                dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
    return dp[n][target]

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = can_partition(nums)
    print('true' if res else 'false')
