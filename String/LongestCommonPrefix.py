
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for char_list in zip(*strs):
            if char_list.count(char_list[0]) == len(char_list):
                prefix += char_list[0]
            else:
                break
        return prefix