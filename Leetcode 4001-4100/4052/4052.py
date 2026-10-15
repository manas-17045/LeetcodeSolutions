# Leetcode 4052: Cyclically Shift Rows and Columns
# https://leetcode.com/problems/cyclically-shift-rows-and-columns/
# Solved on 15th of October, 2026
class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        """
        Cyclically shifts each row to the left and subsequently each column upward.

        Parameters:
            n (int): The dimension size of the n x n grid.
            grid (list[list[int]]): The initial 2D integer matrix.
            rowShift (list[int]): Left shift offsets for each row.
            colShift (list[int]): Upward shift offsets for each column.

        Returns:
            list[list[int]]: The transformed grid after performing all row and column cyclic shifts.
        """
        resultGrid = [[0] * n for _ in range(n)]

        for rowIdx in range(n):
            for colIdx in range(n):
                shiftedCol = (colIdx - rowShift[rowIdx] + n) % n
                shiftedRow = (rowIdx - colShift[rowIdx] + n) % n
                resultGrid[shiftedRow][shiftedCol] = grid[rowIdx][colIdx]

        return resultGrid