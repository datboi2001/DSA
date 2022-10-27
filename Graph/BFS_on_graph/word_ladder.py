from typing import List
from collections import defaultdict, deque

def word_ladder(begin: str, end: str, wordList: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if end not in wordList:
        return 0
    nei = defaultdict(list)
    if begin not in wordList:
        wordList.append(begin)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j+1:]
            nei[pattern].append(word)
    visited = set([begin])
    queue = deque([begin])
    res = 0
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            word = queue.popleft()
            if word == end:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for neiWord in nei[pattern]:
                    if neiWord not in visited:
                        visited.add(neiWord)
                        queue.append(neiWord)
                        
        res += 1
    return 0

if __name__ == '__main__':
    begin = input()
    end = input()
    word_list = input().split()
    res = word_ladder(begin, end, word_list)
    print(res)
