# Leetcode 73: Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Solved on 21st of May, 2025

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        m = len(matrix)
        n = len(matrix[0])

        # Determine if the first row or first column need to zeroed
        first_row_has_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        first_col_has_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use the first row and column as markers for the rest of the matrix.
        # Iterate from matrix[1][1] onwards.
        # If matrix[i][j] is 0, mark matrix[i][0] and matrix[0][j] as 0.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0    # Mark row i to be zeroed
                    matrix[0][j] = 0    # Mark column j to be zeroed

        # Zero out elements in the submatrix (matrix[1:][1:]) based on markers.
        # Iterate from matriz[1][1] onwards.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed (based on its original state).
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0