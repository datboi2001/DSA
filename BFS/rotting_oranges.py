from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
        :param grid: m*n grid where each cell can have one of three values:
            0: empty cell
            1: fresh orange
            2: rotten orange
        :return: the minimum number of minutes that must elapse until no cell has a fresh orange.
        If this is impossible, return -1 instead
        """
        # Idea: BFS

        
        if not grid:
            return -1
        
        def get_valid_coordinates(i, j):
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    yield x, y


        # Step 1: find all rotten oranges

        rotten_oranges = deque()
        fresh_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        # Step 2: BFS
        # 2.1: if there is no rotten orange, return -1
        # 2.2: if there is no fresh orange, return 0

        if not rotten_oranges:
            return -1 if fresh_oranges else 0

        # 2.3: if there are rotten oranges and fresh oranges, start BFS

        minutes = 0
        while rotten_oranges:
            minutes += 1
            for _ in range(len(rotten_oranges)):
                i, j = rotten_oranges.popleft()
                for x, y in get_valid_coordinates(i, j):
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        rotten_oranges.append((x, y))
                        fresh_oranges -= 1
        # Step 3: return minutes - 1 if there is no fresh orange, otherwise return -1
        return -1 if fresh_oranges else minutes - 1 
# Time complexity: O(m*n)
# Space complexity: O(m*n)

print(Solution().orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))
    


