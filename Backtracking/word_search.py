from collections import Counter, defaultdict


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        :param board: two dimensional list of characters
        :param string: a target word
        :return: true if the word exists in the board, false otherwise
        The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
        """
        # Main idea: Backtracking. The main idea is to start from the first character of the word and try
        # to find it in the board. If the first character is found, we can recursively search for the next
        # one in the 4 adjacent cells. The key is to keep track of the visited cells to avoid duplicates.
        # We can use a hash table to store the visited cells. The time complexity is O(mn * 4^k),
        # where m is the number of rows, n is the number of columns, and k is the length of the word.
        # The space complexity is O(mn) for the visited hash table.



        if len(board) == 1 and len(board[0]) == 1 and len(word) == 1:
            return board[0][0] == word[0]

        def dfs(i, j, word):
            if len(word) == 0: # all the characters are checked
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
                return False
            tmp = board[i][j]  # first character is found, check the remaining part
            board[i][j] = "#"  # avoid visit again 
            # check whether can find "word" along one direction
            res = dfs(i+1, j, word[1:]) or dfs( i-1, j, word[1:]) \
            or dfs(i, j+1, word[1:]) or dfs(i, j-1, word[1:])
            board[i][j] = tmp
            return res


        # Iterate over the board and start backtracking
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word):
                    return True
        return False



print(Solution().exist([["a"]], "a"))
