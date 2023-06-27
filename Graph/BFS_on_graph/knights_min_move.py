from collections import deque


def get_knight_shortest_path(x: int, y: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    def get_neighbors(coord):
        res = []
        row, col = coord
        delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
        delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            yield r, c

    def bfs(row: int, col: int) -> int:
        visited = set()
        queue = deque([(row, col)])
        steps = 0
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node[0] == x and node[1] == y:
                    return steps
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            steps += 1

    return bfs(0, 0)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    res = get_knight_shortest_path(x, y)
    print(res)
