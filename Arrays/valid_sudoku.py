from typing import List
class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :param board: a 9x9 sudoku board
        :return: True if the board is valid, False otherwise
        """
        # Main idea: check each row, column, and 3x3 sub-box
        # Time complexity: O(1) since the board is always 9x9
        # Space complexity: O(1) since we only need to store 9 elements in each row, column, and sub-box
        # Check each row
        for row in board:
            seen = set()
            for element in row:
                if element != '.' and element in seen:
                    return False
                seen.add(element)
        # Check each column
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        
        # Check each sub-box
        for i in range(3):
            for j in range(3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        if board[i*3 + k][j*3 + l] != '.' and board[i*3 + k][j*3 + l] in seen:
                            return False
                        seen.add(board[i*3 + k][j*3 + l])
        return True

sudoku_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().isValidSudoku(sudoku_board))
