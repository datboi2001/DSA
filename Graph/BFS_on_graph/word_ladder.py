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

        if end not in wordList or not end or not begin or not wordList:
            return 0
        # Since all words are of same length.
        L = len(begin)
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)
        # Queue for BFS
        print(all_combo_dict)
        queue = deque([(begin, 1)])

        # Visited to make sure we don't repeat processing same word.
        visited = {begin: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == end:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))