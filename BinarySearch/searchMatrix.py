class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])
        l, r = 0, num_rows * num_cols - 1
        while l <= r:
            mid = (l + r) // 2
            # Derive i and j from mid
            i = mid // num_cols
            j = mid - num_cols * i
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False 

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))