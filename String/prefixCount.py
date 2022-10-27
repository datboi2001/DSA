class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        num_words = 0
        for word in words:
            if word.startswith(pref):
                num_words += 1
        return num_words