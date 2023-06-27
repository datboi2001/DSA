class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000}
        result = 0
        i = len(s) - 1
        while i >= 0:
            cur_char = s[i]
            next_char = s[i - 1]
            if i >= 1 and (cur_char in ["V", "X"] and next_char == "I" or\
                    cur_char in ["L", "C"] and next_char == "X" or\
                    cur_char in ["D", "M"] and next_char == "C"):
                result += (roman_map[cur_char] - roman_map[next_char])
                i -= 2
            else:
                result += roman_map[cur_char]
                i -= 1
        return result


test_cases = ["III", 'LVIII', 'MMMCDXC']
solution = Solution()
for test in test_cases:
    print(solution.romanToInt(test))