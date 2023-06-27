class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        raw_str = ""
        for i in s:
            if i.isalnum():
                raw_str += i.lower()
        l, r = 0, len(raw_str)-1
        while l < r:
            if raw_str[l] != raw_str[r]:
                return False
            l += 1
            r -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))