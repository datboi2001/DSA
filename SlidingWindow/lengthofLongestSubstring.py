from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :param s: A string
        :return: The length of the longest substring without repeating characters
        """
        # Idea: Sliding window. We can use a sliding window to solve this problem. The main idea is that
        # we use a counter to count the number of times each character appears in the current window.
        # If the counter of a character is greater than 1, we move the left pointer to the right until
        # the counter of that character is 1. We keep doing this until the right pointer reaches the end
        # of the string. The maximum length of the window is the length of the longest substring without
        # repeating characters.
        

        if not s:
            return 0
        left = 0
        right = 0
        counter = defaultdict(int)
        max_length = 0
        while right < len(s):
            counter[s[right]] += 1
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length

# time complexity: O(n). n is the length of the string. We traverse the string once.
# space complexity: O(n). n is the length of the string. We use a counter to store the number of times

print(Solution().lengthOfLongestSubstring("abcabcbb"))

        