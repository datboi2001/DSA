class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        """
        In a gold mine grid of size m x n, each cell in this mine has an
        integer representing the amount of gold in that cell, 0 if it is empty.
        Return the maximum amount of gold you can collect under the conditions:
        Every time you are located in a cell you will collect all the gold in that cell.
        From your position, you can walk one step to the left, right, up, or down.
        You can't visit the same cell more than once.
        Never visit a cell with 0 gold.
        You can start and stop collecting gold from any position in the grid that has some gold.
        :param grid: Gold mine 
        """
        # Main idea: Backtracking. For each cell in the grid, we do a DFS to find the maximum amount of gold we can
        # collect from that cell. We keep track of the maximum amount of gold we have collected so far and return it
        # at the end.
        
        # Time complexity: O(n * m) where n is the number of rows in the grid and m is the number of columns in the
        # grid
        
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        result = 0

        seen = set()

        def dfs(i, j):
            # If the current cell is out of bounds or is empty or has already been visited, return 0
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or (i, j) in seen:
                return 0
            # Add the current cell to seen
            seen.add((i, j))
            result = grid[i][j]
            # Find the maximum amount of gold we can collect from the four adjacent cells
            result += max(dfs(i + 1, j), dfs(i, j + 1), dfs(i -1, j), dfs(i, j-1)) 
            # Remove the current cell from seen
            seen.remove((i, j))
            return result

        for i in range(n):
            for j in range(m):
                # If the current cell is not empty, do a DFS to find the maximum amount of gold we can collect from
                if grid[i][j] != 0:
                    # Update the result
                    result = max(result, dfs(i, j))
        return result

print(Solution().getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
