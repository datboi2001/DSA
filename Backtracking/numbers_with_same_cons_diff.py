class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        """
        :param n: number of digits
        :param k: difference between consecutive digits
        :return: list of numbers with n digits and consecutive digits with difference k
        """
        res = list(range(1, 10))
        for _ in range(2, n + 1):
            res2 = []
            for num in res:
                last_digit = num % 10
                if last_digit + k < 10:
                    res2.append(num * 10 + last_digit + k)
                if k > 0 and last_digit - k >= 0:
                    res2.append(num * 10 + last_digit - k)
            res = res2
        return res 
    

print(Solution().numsSameConsecDiff(3, 7))
