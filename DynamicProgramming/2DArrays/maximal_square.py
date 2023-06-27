from typing import List


def maximal_square(matrix: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE\
    m, n = len(matrix), len(matrix[0])
    best_side = 0
    # Find the longest side of the square
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 1:
                if r == 0 or c == 0:
                    best_side = max(matrix[r][c], best_side)
                else:
                    matrix[r][c] = 1 + min(matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1])
                    best_side = max(best_side, matrix[r][c])
    return best_side * best_side

    # Top down solution
    # cache = {} # map each (r,c) -> maxLength of square
    #
    # def helper(r, c):
    #     if r >= m or c >= n:
    #         return 0
    #     if (r, c) not in cache:
    #         down = helper(r+1, c)
    #         right = helper(r, c+1)
    #         diagonal = helper(r+1, c+ 1)
    #
    #         cache[(r, c)] = 0
    #         if int(matrix[r][c]) == 1:
    #             cache[(r, c)] = 1 + min(down, right, diagonal)
    #     return cache[(r,c)]
    # helper(0, 0)
    # return max(cache.values()) ** 2


if __name__ == '__main__':
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = maximal_square(matrix)
    print(res)
