from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :param s1: str
        :param s2: str
        :return: True if s2 contains a permutation of s1
        """
        # Main idea: Use a sliding window to check if s2 contains a permutation of s1.
        # Use a dictionary to keep track of the characters in s1.
        # Use a counter to keep track of the number of characters in s1.
        # Time: O(n)
        # Space: O(n)
        # If the length of s1 is greater than s2, then s2 cannot contain a permutation of s1.
        if len(s1) > len(s2):
            return False
        
        # Create a dictionary to keep track of the characters in s1.
        s1_dict = defaultdict(int)
        for char in s1:
            s1_dict[char] += 1
        
        # Create a counter to keep track of the number of characters in s1.
        s1_counter = len(s1_dict)

        # Create a sliding window of length len(s1).
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            # Create a dictionary to keep track of the characters in the sliding window.
            s2_dict = defaultdict(int)
            for char in s2[left:right+1]:
                s2_dict[char] += 1
        
            # Create a counter to keep track of the number of characters in the sliding window.
            s2_counter = len(s2_dict)

            # If the number of characters in the sliding window is equal to the number of characters in s1, then check if the characters in the sliding window are equal to the characters in s1.
            # If the characters in the sliding window are equal to the characters in s1, then return True                     return True
            if s2_counter == s1_counter and s2_dict == s1_dict:
                return True
            # Move the sliding window to the right by 1.
            left += 1
            right += 1
        # If the sliding window does not contain a permutation of s1, then return False.
        return False
