class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        """
        :param s: string
        :param shifts: list of integers where shifts[i] means we want to shift the first i + 1 characters by shifts[i]
        :return: shifted string
        """
        # Main idea: shift the characters in the string by the amount specified in the shifts list. If the shift amount is
        # greater than 26, then we need to wrap around the alphabet.
        # Time complexity: O(n), where n is the length of the string
        # Space complexity: O(n), where n is the length of the string
        s_array = list(s)
        running_sum = []
        for i in range(len(shifts)):
            if i == 0:
                running_sum.append(shifts[i])
            else:
                running_sum.append(running_sum[i - 1] + shifts[i])        


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

        # Shift the characters in the string
        # Time complexity: O(n), where n is the length of the string

        for i in range(len(s_array)):
            if i == 0:
                shift_amount = running_sum[-1]
            else:
                shift_amount = running_sum[-1] - running_sum[i - 1]
            s_array[i] = shift(ord(s_array[i]), shift_amount=shift_amount)
        return "".join(s_array)



print(Solution().shiftingLetters("z", [52]))