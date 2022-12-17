from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: list[list[int]]):
        """
        :param grid: a 2d grid where 1 represents land and 0 represents water
        :return: the number of islands
        """
        n, m = len(grid), len(grid[0])
        def get_neighbors(row: int, col: int):
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r < n and 0 <= c < m:
                    yield r, c
        def bfs(row: int, col: int):
            q = deque([(row, col)])
            while q:
                n = len(q)
                for _ in range(n):
                    cur_row, cur_col = q.popleft()
                    for r, c in get_neighbors(cur_row, cur_col):
                        if grid[r][c] == '1':
                            q.append((r, c))
                            # mark as visited
                            grid[r][c] = '0'
            
        
        res = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1':
                    bfs(row, col)
                    res += 1
        return res


if __name__ == '__main__':
    res = Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
    print(res)
