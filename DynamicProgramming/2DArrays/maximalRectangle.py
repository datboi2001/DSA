class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """
        :param matrix: M*n matrix
        :return: Area of the largest rectangle containing only 1's
        """
        # If the matrix is empty, return 0
        if not matrix:
            return 0
            


print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))