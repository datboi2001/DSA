class Solution:
    def intToRoman(self, num: int) -> str:
        """
        :param num: integer
        :return: roman numeral
        """
        # Main idea: use a dictionary to map the integer to the roman numeral. If the integer is in the dictionary, then
        # return the roman numeral. Otherwise, use the dictionary to find the largest integer that is less than the given
        # integer. Then, subtract the largest integer from the given integer and repeat the process until the given integer
        # is 0.
        # Time complexity: O(n), where n is the number of keys in the dictionary
        # Space complexity: O(1)
        roman_map = {1: "I", 4: "IV",  5: "V", 9: "IX", 10: "X",
            50: "L", 100: "C", 500: "D", 1000: "M", 40: "XL",
            90: "XC", 400: "CD", 900: "CM"}
        if num in roman_map:
            return roman_map[num]
        result = ""

        while num > 0:
            largest = max(x for x in roman_map if x <= num)
            result += roman_map[largest]
            num -= largest
        return result


test_cases = [3, 4, 9, 58, 1994]
solution = Solution()
for test in test_cases:
    print(solution.intToRoman(test))

        