from collections import defaultdict 
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        :param s: str
        :param p: str
        :return array of all the start indices of p's anagrams in s
        """
        if len(s) < len(p):
            return []
        p_counter = defaultdict(int)
        for c in p:
            p_counter[c] += 1
        s_counter = defaultdict(int)
        for c in s[:len(p) - 1]:
            s_counter[c] += 1
        # sCounter is a sliding window of s of length len(p) - 1
        # sCounter is initialized with the first len(p) - 1 characters of s

        result = []
        for i in range(len(p) - 1, len(s)):
            # add the last character of s to sCounter
            s_counter[s[i]] += 1
            # check if sCounter and pCounter are equal
            if s_counter == p_counter:
                # i - len(p) + 1 is the start index of the anagram
                result.append(i - len(p) + 1)
            # remove the first character of sCounter
            s_counter[s[i - len(p) + 1]] -= 1
            if s_counter[s[i - len(p) + 1]] == 0:
                del s_counter[s[i - len(p) + 1]]
        return result

# Time complexity: O(n). n is the length of s. The outer for loop runs n times 
# Space complexity: O(n). n is the length of s. The size of sCounter can grow up to n

print(Solution().findAnagrams("cbaebabacd", "abc"))