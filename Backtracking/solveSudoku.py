from pprint import pprint
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        :param board: a two dimensional sudoku board
        :return: None, modify the board inplace
        """
        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in range(1, 10):
                            if is_valid(i, j, str(k)):
                                board[i][j] = str(k)
                                if backtrack():
                                    return True
                                board[i][j] = "."
                        return False
            return True

        def is_valid(row: int, col: int, c: str) -> bool:
            """
            :param row: The row index
            :param col: The column index
            :param c: The character to be checked
            :return: A boolean indicating if the character is valid at this location
            """
            for i in range(9):
                if board[i][col] == c:
                    return False
                if board[row][i] == c:
                    return False
                box_row = (row // 3) * 3 + i // 3
                box_col = (col // 3) * 3 + i % 3
                if board[box_row][box_col] == c:
                    return False
            return True
        backtrack()
        pprint(board)


Solution().solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
    "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])

