class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        """
        :param matrix: 2d matrix
        """
        self.matrix = matrix
        self.prefix_matrix = [
            [0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        # Idea: prefix_matrix[i][j] = sum of the elements of the matrix from (0, 0) to (i - 1, j - 1) inclusive

        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                # the prefix sum at (i,j) is the sum of the elements of the matrix from (0, 0) to (i - 1, j - 1) inclusive
                # plus the element at (i - 1, j - 1)

                self.prefix_matrix[i][j] = self.prefix_matrix[i-1][j] + \
                    self.prefix_matrix[i][j-1] - \
                    self.prefix_matrix[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        :param row1: int
        :param col1: int
        :param row2: int
        :param col2: int
        :return: sum of the elements of the matrix from (row1, col1) to (row2, col2) inclusive
        """
        # Idea: the sum of the elements of the matrix from (row1, col1) to (row2, col2) inclusive is the sum of the elements of the matrix from (0, 0) to (row2, col2) inclusive
        # minus the sum of the elements of the matrix from (0, 0) to (row1 - 1, col2) inclusive
        # minus the sum of the elements of the matrix from (0, 0) to (row2, col1 - 1) inclusive
        # plus the sum of the elements of the matrix from (0, 0) to (row1 - 1, col1 - 1) inclusive

        return self.prefix_matrix[row2 + 1][col2 + 1] - self.prefix_matrix[row1][col2 + 1] \
            - self.prefix_matrix[row2+1][col1] + self.prefix_matrix[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
