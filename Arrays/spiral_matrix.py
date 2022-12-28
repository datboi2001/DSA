class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        :param matrix: two dimensional array
        :return: one dimensional array that contains all elements in matrix in spiral order
        """

        if not matrix:
            return []
        result = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bottom:
            # top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            # right column
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])
            # bottom row
            if left < right and top < bottom:
                # check if there is a single row or column
                for i in range(right - 1, left, -1):
                    result.append(matrix[bottom][i])
                # left column
                for i in range(bottom, top, -1):
                    result.append(matrix[i][left])
            # move inwards
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return result
    
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
        