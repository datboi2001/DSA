def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    num_rows, num_cols = len(image), len(image[0])
    color = image[r][c]

    def get_neighbors(row, col):
        row_delta = [-1, 0, 1, 0]
        col_delta = [0, 1, 0, -1]
        for i in range(len(row_delta)):
            neighbor_row = row + row_delta[i]
            neighbor_col = col + col_delta[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if image[neighbor_row][neighbor_col] == color:
                    yield neighbor_row, neighbor_col

    def dfs(row, col, visited):
        image[row][col] = replacement
        visited.add((row, col))
        for n_row, n_col in get_neighbors(row, col):
            if (n_row, n_col) in visited:
                continue
            dfs(n_row, n_col, visited)

    dfs(r, c, set())
    return image