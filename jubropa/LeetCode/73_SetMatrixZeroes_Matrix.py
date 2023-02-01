class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        zero_rows_idx_set = set()
        zero_columns_idx_set = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zero_rows_idx_set.add(i)
                    zero_columns_idx_set.add(j)

        for row_idx in zero_rows_idx_set:
            matrix[row_idx] = [0 for _ in range(n)]

        for column_idx in zero_columns_idx_set:
            for i in range(m):
                matrix[i][column_idx] = 0
