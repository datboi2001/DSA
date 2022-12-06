class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        :param s: string 1
        :param t: string 2
        :return: True if s is a subsequence of t, meaning s can be formed
        from t by deleting some or none of the characters without
        disturbing the relative positions of the remaining characters
        """
        if len(s) > len(t):
            return False
        # Use two pointers to compare the characters in s and t
        i, j = 0, 0
        while i < len(s) and j < len(t):
            # if the characters match, move the pointer in s forward
            if s[i] == t[j]:
                i += 1
            # move the pointer in t forward regardless of what happens
            j += 1
        # if the pointer in s reaches the end, s is a subsequence of t
        return i == len(s)