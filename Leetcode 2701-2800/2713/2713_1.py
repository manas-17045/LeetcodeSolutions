# Leetcode 2713: Maximum Strictly Increasing Cells in a Matrix
# https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/
# Solved on 8th of July, 2025
import collections


class Solution:
    def maxIncreasingCells(self, mat: list[list[int]]) -> int:
        """
        Given a 0-indexed m x n integer matrix mat, find the maximum length of a path
        starting from any cell and moving to an adjacent cell (up, down, left, or right)
        such that the value of the destination cell is strictly greater than the value
        of the current cell. You can move multiple times.

        This problem can be solved using dynamic programming.
        The core idea is to process cells in increasing order of their values.
        For each cell (r, c), the maximum path length ending at this cell is
        1 + max(max_path_length_in_row[r], max_path_length_in_col[c]),
        where max_path_length_in_row[r] is the maximum path length ending at any cell
        in row r with a value strictly less than mat[r][c], and similarly for columns.

        Args:
            mat: A list of lists of integers representing the matrix.

        Returns:
            An integer representing the maximum length of a strictly increasing path.
        """
        m = len(mat)
        n = len(mat[0])

        valueToCoords = collections.defaultdict(list)
        for r in range(m):
            for c in range(n):
                valueToCoords[mat[r][c]].append((r, c))

        maxLenRow = [0] * m
        maxLenCol = [0] * n

        sortedValues = sorted(valueToCoords.keys())

        for value in sortedValues:
            coords = valueToCoords[value]
            newPathLengths = []

            for r, c in coords:
                pathLength = 1 + max(maxLenRow[r], maxLenCol[c])
                newPathLengths.append((pathLength, r, c))

            for pathLength, r, c in newPathLengths:
                maxLenRow[r] = max(maxLenRow[r], pathLength)
                maxLenCol[c] = max(maxLenCol[c], pathLength)

        return max(max(maxLenRow), max(maxLenCol))