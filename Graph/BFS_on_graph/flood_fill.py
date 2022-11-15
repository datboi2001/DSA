class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        """
        :param image: Two dim list where image[i][j] is the color of pixel (i, j).
        :param sr: source row
        :param sc: source column
        :param color: new color
        :return: image after flood fill
        """
        cur_color = image[sr][sc]
        if cur_color == newColor:
            return image
        num_row, num_col = len(image), len(image[0])
        visited = {(sr, sc)}

        def get_neighbors(row: int, col: int):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for delta_row, delta_col in directions:
                new_row = row + delta_row
                new_col = col + delta_col
                if 0 <= new_row < num_row and 0 <= new_col < num_col:
                    yield new_row, new_col

        def dfs(row: int, col: int):
            image[row][col] = newColor
            for new_row, new_col in get_neighbors(row, col):
                if image[new_row][new_col] == cur_color and (new_row, new_col) not in visited:
                    dfs(new_row, new_col)
                visited.add((new_row, new_col))
        dfs(sr, sc)
        return image

# Time: O(V+E), where V is the number of nodes and E is the number of edges.
# Space: O(V), where V is the number of nodes.


print(Solution().floodFill(
    image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
