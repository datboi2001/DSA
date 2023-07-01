class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        Given 3 integers a,b, and c, return the minimum number of operations needed to make c equal to a or b.
        Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their
        binary representation.
        :param a: int
        :param b: int
        :param c: int
        :return: int
        """
        # Main idea: use bit manipulation to check if the bit is 1 or 0
        # if the bit is 1, then we need to check if a and b have 0 in that bit
        # if the bit is 0, then we need to check if a or b have 1 in that bit
        # if the bit is 1 and a and b have 0 in that bit, then we need to flip that bit
        # if the bit is 0 and a or b have 1 in that bit, then we need to flip that bit
        # if the bit is 1 and a or b have 1 in that bit, then we don't need to flip that bit


print(Solution().minFlips(2, 6, 5))