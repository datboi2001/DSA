from collections import defaultdict
class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].
        The rank is an integer starting from 1. If two elements p and q are in the same row or column, then:
        If p < q then rank(p) < rank(q)
        If p == q then rank(p) == rank(q)
        If p > q then rank(p) > rank(q)
        :param matrix: a matrix of integers
        :return: a matrix of integers where each element is the rank of the element
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        # Create a dictionary of values to rows and columns
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[matrix[i][j]].append((i, j))
        # Create a dictionary of rows and columns to ranks
        r = defaultdict(int)
        c = defaultdict(int)
        # Iterate through the dictionary of values to rows and columns
        for v in sorted(d):
            # Create a set of rows and columns that have been visited
            visited = set()
            # Iterate through the rows and columns
            for i, j in d[v]:
                # Find the maximum rank of the row and column
                rank = max(r[i], c[j])
                # If the row and column have not been visited, increment the rank
                if (i, j) not in visited:
                    rank += 1
                # Update the rank of the row and column
                r[i] = rank
                c[j] = rank
                # Add the row and column to the set of visited rows and columns
                visited.add((i, j))
            # Iterate through the rows and columns
            for i, j in d[v]:
                # Update the rank of the row and column
                r[i] = c[j] = max(r[i], c[j])
        # Create a matrix of ranks
        ans = [[0] * n for _ in range(m)]
        # Iterate through the rows and columns
        for i in range(m):
            for j in range(n):
                # Update the rank of the row and column
                ans[i][j] = r[i]
        return ans