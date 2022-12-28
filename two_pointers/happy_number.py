class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determine if n is happy.
        A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
        :param n: int
        :return: bool
        """
        def get_next(n: int):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total
        
        seen = {}

        while n != 1 and n not in seen:
            seen[n] = True
            n = get_next(n)
        return n == 1


print(Solution().isHappy(2))

