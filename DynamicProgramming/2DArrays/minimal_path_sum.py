from typing import List

def min_path_sum(grid: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if j == 0 and i == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]

if __name__ == '__main__':
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = min_path_sum(grid)
    print(res)
