from typing import List
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        """
        A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence 
        of words beginWord -> s1 -> s2 -> ... -> sk such that:
        - Every adjacent pair of words differs by a single letter.
        - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
        - sk == endWord
        Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
        transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
        :param begin: begin word
        :param end: end word
        :param wordList: list of words
        :return: number of words in the shortest transformation sequence from beginWord to endWord
        """
        # WRITE YOUR BRILLIANT CODE HERE
        # Idea: BFS on the graph. For each word, we create a graph where each node is a word and each edge is a word
        # that is one edit distance away from the current word. We then do BFS on the graph to find the shortest path
        # from beginWord to endWord
        # Time complexity: O(n * m^2) where n is the number of words in wordList and m is the length of each word
        # Space complexity: O(n * m^2)

        # Create a graph where each node is a word and each edge is a word that is one edit distance away from the
        # current word
        if end not in wordList:
            return 0
        # Add beginWord to wordList
        wordList.append(begin)

        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # Create a new word by replacing each character in word with a *
                graph[word[:i] + "*" + word[i + 1:]].append(word)
        
        # Do BFS on the graph to find the shortest path from beginWord to endWord
        queue = deque([(begin, 1)])
        visited = set()
        while queue:
            word, dist = queue.popleft()
            # If we have reached the end word, return the distance
            if word == end:
                return dist
            # Add all the words that are one edit distance away from the current word to the queue
            for i in range(len(word)):
                # Create a new word by replacing each character in word with a *
                for w in graph[word[:i] + "*" + word[i + 1:]]:
                    if w not in visited:
                        visited.add(w)
                        queue.append((w, dist + 1))
        return 0

print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))