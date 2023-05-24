from typing import List

def min_path_sum(grid: List[List[int]]) -> int:
    """
    :param grid: two dimensional array of integers
    :return: minimum path sum
    """
    # Main idea: dynamic programming. We start from  the top left corner and move to the bottom right corner.
    # At each step we can move either right or down. We need to find the path with the minimum sum.
    # We can use a 2D array to store the minimum sum at each step. The minimum sum at each step is the minimum of
    # the sum of the current cell and the sum of the cell above it or the sum of the current cell and the sum of the
    # cell to the left of it. The minimum sum at the bottom right corner is the minimum path sum.
    # Time complexity: O(mn)
    # Space complexity: O(1)
    if len(grid) == 0:
        return 0
    if len(grid) == 1 and len(grid[0]) == 1:
        return grid[0][0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                continue 
            else:
                # The minimum sum at each step is the minimum of the sum of the current cell and the sum of the cell
                0# above it or the sum of the current cell and the sum of the cell to the left of it
                # If we are at the first row, we can only move right
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                # If we are at the first column, we can only move down
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                # If we are not at the first row or the first column, we can move either right or down
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]

if __name__ == '__main__':
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = min_path_sum(grid)
    print(res)
