class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        :param s: string 1
        :param t: string 2
        :return: True if s and t are isomorphic, meaning the characters in s
        can be replaced to get t
        """
        if len(s) != len(t):
            return False
        # Create two dictionaries to store the mapping from s to t and t to s
        s_to_t = {}
        t_to_s = {}
        for i in range(len(s)):
            if s[i] not in s_to_t:
                s_to_t[s[i]] = t[i]
            if t[i] not in t_to_s:
                t_to_s[t[i]] = s[i]
            if s_to_t[s[i]] != t[i] or t_to_s[t[i]] != s[i]:
                # if the mapping is not one-to-one, return False
                return False
        return True

print(Solution().isIsomorphic("paper" , "title"))