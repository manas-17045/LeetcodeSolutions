# Leetcode 3402: Minimum Operations to Make Columns Strictly Increasing
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/
# Solved on 9th of October, 2025
class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum number of operations to make each column in the grid strictly increasing.

        Args:
            grid: A 2D list of integers representing the grid.
        Returns:
            The total minimum operations required.
        """
        numRows = len(grid)
        numCols = len(grid[0])
        totalOperations = 0

        for colIndex in range(numCols):
            previousValue = grid[0][colIndex]
            for rowIndex in range(1, numRows):
                currentValue = grid[rowIndex][colIndex]

                newValue = max(currentValue, previousValue + 1)

                operationsForCell = newValue - currentValue
                totalOperations += operationsForCell

                previousValue = newValue

        return totalOperations