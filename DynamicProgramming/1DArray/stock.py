class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        :param prices: integer array that contains the price of a given stock
        :param Maximum profit or 0 if you cannot achieve any profit
        """
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
