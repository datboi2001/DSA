from math import log10, ceil
class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        :param n: The nth digit to find in an infinite sequence from 1 to n
        :return: The nth digit
        """
        # Main idea: Find the number that contains the nth digit. Then find the nth digit in that number.
        # The number of digits in a number with n digits is 9 * 10^(n-1)



print(Solution().findNthDigit(11))
