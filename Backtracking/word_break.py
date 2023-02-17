from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict: set[str] = set(wordDict)
        # dp[i] is True if s[:i] can be segmented into words in wordDict
        dp = [False] * (len(s) + 1)
        # Base case: empty string can be segmented into words in wordDict
        dp[0] = True
        # Loop through all possible end indices of s
        for i in range(len(s) + 1):
            for j in range(i):
                # If s[:j] can be segmented into words in wordDict and s[j:i] is a word in wordDict
                if dp[j] and s[j:i] in wordDict:
                    # Then s[:i] can be segmented into words in wordDict
                    dp[i] = True
                    # No need to continue the inner loop
                    break
        return dp[-1]
       


if __name__ == '__main__':
    ...
    # s = input()
    # words = input().split()
    # res = word_break(s, words)
    # print('true' if res else 'false')
