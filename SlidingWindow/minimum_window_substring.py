from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        :param s: A string
        :param t: A string
        :return: The minimum substring of s that contains all the characters in t.
        If there is no such substring, return the empty string
        """
        if s == t:
            return s
        # Idea: Use a sliding window to find the minimum substring of s that contains all the characters in t.
        # The main idea is that we use a sliding window to find the minimum substring of s that contains all the characters
        # in t. We use a dictionary to store the characters in t. We use a counter to count the number of characters in t
        # that are in the sliding window. We use a variable to store the minimum length of the substring. 

        # Initialize the dictionary to store the characters in t.
        t_dict: dict[str, int] = defaultdict(int)
        for char in t:
            t_dict[char] += 1
        # Initialize the counter to count the number of characters in t that are in the sliding window.
        counter = len(t)
        # Initialize the minimum length of the substring.
        min_length = len(s) + 1
        # Initialize the left and right pointers of the sliding window.
        left = 0
        right = 0
        # Initialize the start and end indices of the minimum substring.
        start = 0
        end = 0
        # Use a sliding window to find the minimum substring of s that contains all the characters in t.
        while right < len(s):
            # If the character at the right pointer is in the dictionary, we decrement the counter.
            if s[right] in t_dict:
                t_dict[s[right]] -= 1
                # If the character at the right pointer is in the dictionary and the value of the character is greater
                # than or equal to 0, we decrement the counter. 
                if t_dict[s[right]] >= 0:
                    counter -= 1
            # If the counter is 0, we have found a substring that contains all the characters in t. We update the
            # minimum length of the substring and the start and end indices of the minimum substring.
            if counter == 0:
                while left <= right:
                    # If the character at the left pointer is in the dictionary, we increment the counter.
                    if s[left] in t_dict:
                        t_dict[s[left]] += 1
                        # If the character at the left pointer is in the dictionary and the value of the character is
                        # greater than 0, we increment the counter.
                        if t_dict[s[left]] > 0:
                            counter += 1
                            # If the length of the substring is less than the minimum length of the substring, we update
                            # the minimum length of the substring and the start and end indices of the minimum substring.
                            cur_min_length = right - left + 1
                            if cur_min_length < min_length:
                                min_length = cur_min_length
                                start = left
                                end = right
                            left += 1
                            break
                    left += 1
            right += 1
        # If the minimum length of the substring is greater than the length of s, we return the empty string.
        if min_length > len(s):
            return ""
        # Otherwise, we return the minimum substring of s that contains all the characters in t.
        return s[start:end + 1]


print(Solution().minWindow("ADOBECODEBANC", "ABC"))


