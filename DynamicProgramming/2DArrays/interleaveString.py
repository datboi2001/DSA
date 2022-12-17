from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def recursion(s1_i, s2_j, s3_k) -> bool:
            if s1_i == len(s1):
                # s1 is empty
                return s2[s2_j:] == s3[s3_k:]
            if s2_j == len(s2):
                # s2 is empty
                return s1[s1_i:] == s3[s3_k:]
            if s1[s1_i] == s3[s3_k] and s2[s2_j] == s3[s3_k]:
                # both s1 and s2 have the same char
                return recursion(s1_i + 1, s2_j, s3_k + 1) or recursion(
                    s1_i, s2_j + 1, s3_k + 1)
            elif s1[s1_i] == s3[s3_k]:
                # s1 has the same char
                return recursion(s1_i + 1, s2_j, s3_k + 1)
            elif s2[s2_j] == s3[s3_k]:
                # s2 has the same char
                return recursion(s1_i, s2_j + 1, s3_k + 1)
            else:
                return False

        return recursion(0, 0, 0)
    

print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
