from typing import List
from collections import deque
def count_number_of_islands(grid: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    num_cols, num_rows = len(grid[0]), len(grid)

    def get_neighbors(coord: (int, int)):
        row, col = coord
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                yield r, c

    def bfs(start):
        queue = deque([start])
        r, c = start
        grid[r][c] = 0
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                r, c = neighbor
                if grid[r][c] == 0:
                    continue
                queue.append(neighbor)
                grid[r][c] = 0

    count = 0
    # bfs starting from each unvisited land cell
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                continue
            bfs((r, c))
            count += 1  # bfs would find 1 connected island, increment count
    return count


if __name__ == '__main__':
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)
