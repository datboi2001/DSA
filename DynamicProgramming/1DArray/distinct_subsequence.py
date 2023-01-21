from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        :param s: string
        :param t: string
        :return: number of distinct subsequences of s which equals t
        """
        # Main idea: dynamic programming. We start from the first character of s and t. If the characters are equal,
        # we can either include the character in the subsequence or exclude it. If the characters are not equal, we
        # can only exclude the character from the subsequence. We can use a 2D array to store the number of distinct
        # subsequences at each step. The number of distinct subsequences at each step is the sum of the number of
        # distinct subsequences of the substring of s without the current character and the substring of t without
        # the current character if the characters are equal or the number of distinct subsequences of the substring
        # of s without the current character if the characters are not equal. The number of distinct subsequences at
        # the end of s is the number of distinct subsequences of s which equals t.

        # Time complexity: O(mn)
        # Space complexity: O(mn)

        if len(s) == 0 or len(t) == 0:
            return 0
        if len(s) < len(t):
            return 0
        if len(s) == len(t):
            return int(s == t)
        @cache
        def num_distinct_recursion(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if s[i] == t[j]:
                return num_distinct_recursion(i + 1, j + 1) + num_distinct_recursion(i + 1, j)
            else:
                return num_distinct_recursion(i + 1, j)

        return num_distinct_recursion(0, 0)

if __name__ == '__main__':
    s = 'rabbbit'
    t = 'rabbit'
    res = Solution().numDistinct(s, t)
    print(res)