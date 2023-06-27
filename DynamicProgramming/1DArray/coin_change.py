from functools import cache
from sys import maxsize
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        :param coins: an array representing the different values of coins in your possession.
        You may assume you have an infinite number of each kind of coin
        :param amount: the amount of money you want to make change for
        :return: the fewest number of coins that you need to make up that amount.
        If that amount of money cannot be made up by any combination of the coins, return -1
        """
        # Idea: Dynamic Programming. We can use dynamic programming to solve this problem. The main
        # idea is that if we want to make change for amount n, we can use the coins that are less than
        # or equal to n. So the minimum number of coins we need to make change for amount n is the minimum
        # of the following two cases:
        # 1. We use the coin that is equal to n
        # 2. We use the coin that is less than n and make change for amount n - coin

        # Solve with recursion 
        @cache
        def coin_recursion(n: int):
            # Base case
            if n == 0:
                return 0
            if n < 0:
                return -1
            # Recursive case
            result = float('inf')
            for coin in coins:
                sub_result = coin_recursion(n - coin)
                if sub_result >= 0:
                    result = min(result, sub_result + 1)
            return result if result != float('inf') else -1

        # Solve with dynamic programming
        def coin_dp() -> int:
            dp = [maxsize] * (amount + 1) 
            dp[0] = 0
            # dp[i] is the minimum number of coins we need to make change for amount i
            for i in range(1, amount + 1):
                for coin in coins:
                    if i >= coin:
                        # If we can make change for amount i - coin, we can make change for amount i
                        dp[i] = min(dp[i], dp[i - coin] + 1)
            return dp[amount] if dp[amount] != maxsize else -1
        
        return coin_dp()

print(Solution().coinChange([1, 2, 5], 11))

# Time complexity: O(n * m) where n is the amount and m is the number of coins
# Space complexity: O(n)
