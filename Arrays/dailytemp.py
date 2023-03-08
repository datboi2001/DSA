class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        :param temperatures: list of daily temperatures
        :return: list of number of days to wait until a warmer temperature
        """
        # Main idea: use a stack to keep track of the indices of the temperatures
        # that are smaller than the current temperature
        n = len(temperatures)
        if n == 1:
            return [0]
        ans = [0] * n
        stack = []
        for i in range(n):
            # pop all the temperatures that are smaller than the current temperature
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans
