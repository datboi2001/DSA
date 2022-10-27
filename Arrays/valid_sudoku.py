from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        solution = board
        N, p, q = 9, 3, 3
        for i in range(N):
            unique_vals = set()
            for j in range(N):
                if solution[i][j] != ".":
                    if solution[i][j] not in unique_vals:
                        unique_vals.add(solution[i][j])
                    else:
                        return False
        # checks cols
        for j in range(N):
            unique_vals = set()
            for i in range(N):
                if solution[i][j] != ".":
                    if solution[i][j] not in unique_vals:
                        unique_vals.add(solution[i][j])
                    else:
                        return False
        # checks boxes
        for i in range(q):
            for j in range(p):
                unique_vals = set()
                for k in range(p):
                    for l in range(q):
                        if solution[i * p + k][j * q + l] != ".":
                            if solution[i * p + k][j * q + l] not in unique_vals:
                                unique_vals.add(solution[i * p + k][j * q + l])
                            else:
                                return False
        return True


sudoku_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().isValidSudoku(sudoku_board))
