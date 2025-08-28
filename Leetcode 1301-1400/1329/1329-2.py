# Leetcode 1329: Sort the Matrix Diagonally
# https://leetcode.com/problems/sort-the-matrix-diagonally/
# Solved on 28th of August, 2025
class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        """
        Sorts each diagonal of the given matrix in ascending order.
        :param mat: The input matrix of integers.
        :return: The matrix with all its diagonals sorted.
        """
        m = len(mat)
        if m == 0:
            return mat
        n = len(mat[0])

        # Process all diagonals that start on the first row
        for start_col in range(n):
            self.sort_diagonal(mat, 0, start_col, m, n)

        # Process all diagonals that start on the first column (except the very first cell)
        for start_row in range(1, m):
            self.sort_diagonal(mat, start_row, 0, m, n)

        return mat

    def sort_diagonal(self, mat: list[list[int]], r: int, c: int, m: int, n: int) -> None:
        # Counting sort for values in range 1...100 (constraints)
        counts = [0] * 101
        i, j = r, c
        # Count values on this diagonal
        while i < m and j < n:
            counts[mat[i][j]] += 1
            i += 1
            j += 1
        # Write back sorted values
        val = 1
        i, j = r, c
        while i < m and j < n:
            # Find next available value
            while val <= 100 and counts[val] == 0:
                val += 1
            # Place value
            mat[i][j] = val
            counts[val] -= 1
            i += 1
            j += 1