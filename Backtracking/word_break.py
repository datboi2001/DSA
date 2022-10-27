from typing import List

def word_break(s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for word in wordDict:
            if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                dp[i] = dp[i + len(word)]
            if dp[i]:
                break
    return dp[0]



if __name__ == '__main__':
    s = input()
    words = input().split()
    res = word_break(s, words)
    print('true' if res else 'false')
