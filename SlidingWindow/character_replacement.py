class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
        :param s: str
        :param k: int
        :return: length of the longest substring containing the same letter you can get after performing the above operations. 
        """
        # Idea: sliding window. The size of the sliding window is the length of the substring.
        # The number of characters that need to be replaced is the length of the sliding window
        # minus the max frequency of a character in the sliding window.
        # If the number of characters that need to be replaced is greater than k,
        # we need to remove the first character of the sliding window.
        # Time complexity: O(n). n is the length of s. The outer while loop runs n times
        # Space complexity: O(1). The size of freq is constant

        if len(s) == 0:
            return 0
        
        # sliding window
        start = 0
        end = 0
        # max frequency of a character in the sliding window
        max_freq = 0
        # frequency of each character in the sliding window
        freq = {}
        while end < len(s):
            # add the last character of s to freq
            freq[s[end]] = freq.get(s[end], 0) + 1
            # update max_freq
            max_freq = max(max_freq, freq[s[end]])
            # if the number of characters that need to be replaced is greater than k
            if end - start + 1 - max_freq > k:
                # remove the first character of freq
                freq[s[start]] -= 1
                # update start
                start += 1
            # update end
            end += 1
        return end - start
    
print(Solution().characterReplacement("AABABBA", 1))
