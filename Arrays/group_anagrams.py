from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        :param strs: an array of strings
        :return: A list of a group of anagrams 
        """ 
        # Main idea: use a dictionary to store the anagrams. The key is the sorted string, 
        # and the value is a list of anagrams.
        # Time complexity: O(n)        

        anagrams = defaultdict(list) 
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
        return list(anagrams.values())
