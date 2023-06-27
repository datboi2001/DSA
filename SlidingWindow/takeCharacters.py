from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
        :param s: string
        :param k: integer
        :return: minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
        """

        # Main idea: use a sliding window to keep track of the number of characters in the window. If the number of characters
        # in the window is less than k, then we need to expand the window. If the number of characters in the window is greater
        # than or equal to k, then we need to shrink the window.

        if not s:
            return 0
        if k > len(s):
            return -1

        # Use a dictionary to keep track of the number of characters in the window
        freq = Counter(s)
        if freq['a'] < k or freq['b'] < k or freq['c'] < k:
            return -1
        
        left = len(s) -1 
        right = len(s) - 1
        ans = len(s)
        while left >=0 :
            freq[s[left]] -= 1
            while freq['a'] < k or freq['b'] < k or freq['c'] < k:
                freq[s[right]] += 1
                right -= 1
            ans = min(ans, left + (len(s) - 1 - right) )

            left -= 1
        return ans


print(Solution().takeCharacters("aabaaaacaabc", 2))