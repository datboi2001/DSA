class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        min_price = 10**4
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if (prices[i] - min_price) > maximum:
                maximum = prices[i] - min_price
        return maximum