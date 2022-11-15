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
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        result = 0
        total = sum(sum(row) for row in grid)
        def dfs(row: int, col: int, max_sum: int, seen: set[tuple[int, int]]):
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == 0 or (row, col) in seen:
                return max_sum
            seen.add((row, col))
            max_sum += grid[row][col]
            mx = 0
            directions = [[row + 1, col], [row-1, col],
                          [row, col + 1], [row, col - 1]]
            for new_row, new_col in directions:
                mx = max(mx, dfs(new_row, new_col, max_sum, seen))
            seen.discard((row, col))
            return mx

        for row in range(n):
            for col in range(m):
                if grid[row][col] > 0:
                    result = max(result, dfs(row, col, 0, set()))
                    if result == total:
                        return total
        return result


print(Solution().getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
