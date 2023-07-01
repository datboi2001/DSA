from collections import Counter
from string import ascii_lowercase
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # main idea: use Counter to count the number of each character in each word
        # then, find the minimum number of each character in each word
        # Time: O(n) where n is the length of words
        # Space: O(n) where n is the length of words
        ans = []
        # create a Counter for each word
        counters = [Counter(word) for word in words]
        # create a Counter for the minimum number of each character in each word
        min_counters = Counter()
        for char in ascii_lowercase:
            min_counters[char] = min(counter[char] for counter in counters)
        # add the minimum number of each character in each word to ans
        for char in min_counters:
            ans.extend(char * min_counters[char])
        return ans
         
    

print(Solution().commonChars(["bella","label","roller"]))