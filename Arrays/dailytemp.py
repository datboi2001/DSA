class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        :param temperatures: list of daily temperatures
        :return: list of number of days to wait until a warmer temperature
        """
        n = len(temperatures)
        if n == 1:
            return [0]
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans
