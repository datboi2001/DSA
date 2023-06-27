class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        Find the maximum profit you can achieve. You may complete at most two transactions.
        Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
        :param prices: a list of integers
        :return: the maximum profit
        """
        
        # Main idea: Dynamic Programming. We can use dynamic programming to solve this problem. The main idea is that
        # if we want to find the maximum profit, we can use the prices that are less than or equal to the current
        # prices. So the maximum profit is the maximum of the following two cases:
        # 1. We use the price that is equal to the current price
        # 2. We use the price that is less than the current price and find the maximum profit of the remaining prices
        #
        # We can use the following two arrays to store the maximum profit of the remaining prices:
        # 1. left[i] is the maximum profit of the remaining prices on the left of the ith price
        # 2. right[i] is the maximum profit of the remaining prices on the right of the ith price


        left = [0 for _ in range(len(prices))]
        right = [0 for _ in range(len(prices))]


        # left[i] is the maximum profit of the remaining prices on the left of the ith price
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            left[i] = max(left[i-1], prices[i] - min_price)
        
        # right[i] is the maximum profit of the remaining prices on the right of the ith price
        max_price = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right[i] = max(right[i+1], max_price - prices[i])
        
        # The maximum profit is the maximum of the following two cases:
        # 1. We use the price that is equal to the current price
        # 2. We use the price that is less than the current price and find the maximum profit of the remaining prices
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, left[i] + right[i])
        return max_profit
        

print(Solution().maxProfit([1,2,3,4,5]))