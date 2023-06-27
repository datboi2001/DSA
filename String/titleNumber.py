class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, char in enumerate(columnTitle[::-1]):
            result += (ord(char) - 64) * (26 ** i)
        return result

print(Solution().titleToNumber('ZY'))