class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
        :param prices: List of prices
        :return: Maximum profit
        """
        if len(prices) == 0:
            return 0
        # dp[i] = max profit on day i
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            # dp[i] = max profit on day i
            # dp[i-1] = max profit on day i-1
            # prices[i] = price on day i
            # prices[i-1] = price on day i-1
            # dp[i-1] + prices[i] - prices[i-1] = max profit on day i if we buy on day i-1 and sell on day i
            dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1])
        return dp[-1]

print(Solution().maxProfit([7,1,5,3,6,4]))
