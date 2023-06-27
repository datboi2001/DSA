from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        :param s: string that consists of lowercase or uppercase letters
        :return: Length of longest palindrome that can be built with those letters
        """
        count = Counter(s)
        ans = 0
        for v in count.values():
            # if v is even, we can use it to build the palindrome
            ans += v // 2 * 2
            # if v is odd, we can use it to build the palindrome
            # if ans is even, we can add 1 to make it odd
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
