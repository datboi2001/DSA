from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        """
        Longest Palindrome by Concatenating Two Letter Words
        You are given an array of strings. Each element of this array consists of two lowercase English letters.
Create the longest possible palindrome by selecting some elements from array and concatenating them in any order.
Each element can be selected at most once.
Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
        :param words: list of strings where each string consists of two lowercase English letters
        :return: length of longest palindrome that can be built with those strings by concatenating them in any order
        """
        # Idea: Use a dictionary to store the frequency of each letter

        # Create a dictionary to store the frequency of each letter
        freq = defaultdict(int)
        unpaired = ans = 0
        for word in words:
            if word[0] == word[1]:
                if freq[word] > 0:
                    unpaired -= 1
                    freq[word] -= 1
                    ans += 4
                else:
                    unpaired += 1
                    freq[word] += 1
            else:
                if freq[word[::-1]] > 0:
                    ans += 4
                    freq[word[::-1]] -= 1
                else:
                    freq[word] += 1
        if unpaired > 0:
            ans += 2
        return ans



print(Solution().longestPalindrome(["lc", "cl", "gg"]))
