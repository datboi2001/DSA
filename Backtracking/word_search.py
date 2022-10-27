from collections import Counter, defaultdict


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        :param board: two dimensional list of characters
        :param string: a target word
        :return: true if the word exists in the board, false otherwise
        """
        def backtrack(i: int, j: int, index: int) -> bool:
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[index] != board[i][j]:
                return False
            if index == len(word) - 1:
                return True
            temp = board[i][j]
            board[i][j] = '#'
            result = backtrack(i + 1, j, index + 1) or backtrack(i - 1, j, index +
                                                                 1) or backtrack(i, j + 1, index + 1) or backtrack(i, j - 1, index + 1)
            if result:
                return True
            board[i][j] = temp
        if not board:
            return False
        if not word:
            return False
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1

        # Count number of letters in word
        # Check if board has all the letters in the word and they are atleast same count from word
        wordDic = Counter(word)
        for c in wordDic:
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False


print(Solution().exist([["A", "B", "C", "E"], [
      "S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))
