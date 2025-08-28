# Leetcode 1329: Sort the Matrix Diagonally
# https://leetcode.com/problems/sort-the-matrix-diagonally/
# Solved on 28th of August, 2025
import collections


class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        """
        Sorts the matrix diagonally.

        For each diagonal, all elements are extracted, sorted, and then placed back into the matrix.
        The key for each diagonal is `rowIndex - colIndex`.

        Args:
            mat: The input matrix (list of lists of integers).
        Returns:
            The diagonally sorted matrix.
        """
        numRows = len(mat)
        numCols = len(mat[0])

        diagonals = collections.defaultdict(list)

        for rowIndex in range(numRows):
            for colIndex in range(numCols):
                diagonals[rowIndex - colIndex].append(mat[rowIndex][colIndex])

        for key in diagonals:
            diagonals[key].sort(reverse=True)

        for rowIndex in range(numRows):
            for colIndex in range(numCols):
                mat[rowIndex][colIndex] = diagonals[rowIndex - colIndex].pop()

        return mat