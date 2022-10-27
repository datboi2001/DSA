
class Solution:
        
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        """
        :param n: number of digits
        :param k: difference between consecutive digits
        :return: list of numbers with n digits and consecutive digits with difference k
        """
        def dfs(n: int, k: int, i: int, res: list[int]):
            if n == 0:
                res.append(i)
                return
            last_digit = i % 10
            if last_digit - k >= 0:
                dfs(n - 1, k, i * 10 + last_digit - k, res)
            if k > 0 and last_digit + k <= 9:
                dfs(n - 1, k, i * 10 + last_digit + k, res)
        res = []
         
        for i in range(1, 10):
            # start with 1, 2, ..., 9
            dfs(n - 1, k, i, res)
        return res
print(Solution().numsSameConsecDiff(3, 7))
