from collections import defaultdict
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        """
        :param s: string
        :param shifts: list of lists where shifts[i] = [start, end, direction] means we want to shift the characters
        between start and end (inclusive) by direction. If direction is 1, then we want to shift the characters to the right. If
        direction is 0, then we want to shift the characters to the left.
        :return: shifted string
        """
        # Main idea: Prefix sum. We want to keep track of the shift amount for each character in the string. If the shift
        # amount is negative, then we want to shift the character to the left. If the shift amount is positive, then we want
        # to shift the character to the right.
        s_array = list(s)
        line = [0] * (len(s_array) + 1)
        for start, end, direction in shifts:
            if direction == 1:
                # Shift the characters to the right
                line[start] += 1
                # We need to subtract 1 from the character after the end of the range because we don't want to shift the
                # character at the end of the range.
                line[end + 1] -= 1
            else:
                # Shift the characters to the left
                line[start] -= 1
                # We need to add 1 to the character after the end of the range because we don't want to shift the
                # character at the end of the range.
                line[end + 1] += 1
            
        # Calculate the prefix sum
        for i in range(1, len(line)):
            line[i] += line[i - 1]

        def shift(char_val: int, shift_amount: int) -> str:
            """
            Note that shift_amount can be greater than 26. If it is, then we need to wrap around the alphabet.
            :param char_val: integer value of a character
            :param shift_amount: amount to shift the character
            :return: shifted character
            """
            # Main idea: shift the character by the shift amount. If the character is greater than 'z', then we need to wrap
            # around the alphabet.
            # Time complexity: O(1)
            # Space complexity: O(1)
            if shift_amount > 26:
                shift_amount = shift_amount % 26
            char_val += shift_amount
            if char_val > ord('z'):
                char_val -= 26
            return chr(char_val)
        
        for i in range(len(s_array)):
            shift_amount = line[i]
            if shift_amount < 0:
                shift_amount %= 26
            s_array[i] = shift(ord(s_array[i]), shift_amount=shift_amount)

        return "".join(s_array)