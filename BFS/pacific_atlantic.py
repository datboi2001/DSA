from collections import deque
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
        :param heights: m*n matrix where each cell has a height
        :return: a list of coordinates where rain water can flow from cell to both the Pacific and Atlantic oceans
        """
        # Idea: BFS from ocean cells
        # Ocean cells are cells that are on the border of the matrix
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n-1))
        for j in range(n):
            pacific.add((0, j))
            atlantic.add((m-1, j))
        
        def get_valid_coordinates(i, j):
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n:
                    yield x, y

        def bfs(ocean):
            """
            :param ocean: a set of coordinates of ocean cells
            :return: a set of coordinates of cells that can flow to the ocean
            """
            queue = deque(ocean)
            while queue:
                i, j = queue.popleft()
                for x, y in get_valid_coordinates(i, j):
                    if (x, y) not in ocean and heights[x][y] >= heights[i][j]:
                        ocean.add((x, y))
                        queue.append((x, y))
            return ocean
        
        # BFS from ocean cells
        pacific = bfs(pacific)
        atlantic = bfs(atlantic)
        return [[x,y] for x,y in pacific & atlantic]

# Time complexity: O(m*n)
# Space complexity: O(m*n)

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) 