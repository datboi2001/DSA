from typing import Iterator 
from collections import deque

class Solution:
    def numIslands(self, grid: list[list[int]]):
        """
        :param grid: a 2d grid where 1 represents land and 0 represents water
        :return: the number of islands
        """
        n, m = len(grid), len(grid[0])
        # Idea: Use BFS to traverse the grid
        # Time complexity: O(nm)
        # Space complexity: O(nm)
        def get_neighbors(row: int, col: int) -> Iterator[tuple[int, int]]:
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r < n and 0 <= c < m:
                    yield r, c
        def bfs(row: int, col: int):
            # Put the starting point in the queue
            q = deque([(row, col)])
            while q:
                n = len(q)
                for _ in range(n):
                    # Pop the first element in the queue
                    cur_row, cur_col = q.popleft()
                    for r, c in get_neighbors(cur_row, cur_col):
                        # If the neighbor is land, put it in the queue
                        if grid[r][c] == '1':
                            q.append((r, c))
                            # mark as visited
                            grid[r][c] = '0'
        res = 0
        # Traverse the grid
        for row in range(n):
            for col in range(m):
                # If the current cell is land, do a BFS
                if grid[row][col] == '1':
                    bfs(row, col)
                    # Increment the number of islands
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
