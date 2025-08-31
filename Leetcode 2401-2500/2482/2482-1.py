# Leetcode 2482: Difference Between Ones and Zeros in Row and Column
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
# Solved on 31st of August, 2025
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Calculates the difference between the number of ones and zeros in each row and column.

        For each cell (i, j), the value in the resulting matrix `diff` is calculated as:
        diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]

        Args:
            grid: A 2D list of integers (0s and 1s) representing the input grid.
        Returns:
            A 2D list of integers representing the difference matrix.
        """
        numRows = len(grid)
        numCols = len(grid[0])

        onesInRow = [0] * numRows
        onesInCol = [0] * numCols

        for r in range(numRows):
            for c in range(numCols):
                onesInRow[r] += grid[r][c]
                onesInCol[c] += grid[r][c]

        diff = [[0] * numCols for _ in range(numRows)]

        for r in range(numRows):
            for c in range(numCols):
                diff[r][c] = 2 * onesInRow[r] + 2 * onesInCol[c] - numRows - numCols

        return diff