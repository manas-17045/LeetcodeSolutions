# Leetcode 3195: Find the Minimum Area to Cover All Ones I
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/
# Solved on 22nd of August, 2025
class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        """
        Finds the minimum area of a rectangle that covers all '1's in a binary grid.

        Args:
            grid (list[list[int]]): A 2D binary grid where 1 represents an occupied cell and 0 an empty cell.
        Returns:
            int: The minimum area required to cover all '1's.
        """
        numRows = len(grid)
        numCols = len(grid[0])

        minRow = numRows
        maxRow = -1
        minCol = numCols
        maxCol = -1

        for rowIndex in range(numRows):
            for colIndex in range(numCols):
                if grid[rowIndex][colIndex] == 1:
                    minRow = min(minRow, rowIndex)
                    maxRow = max(maxRow, rowIndex)
                    minCol = min(minCol, colIndex)
                    maxCol = max(maxCol, colIndex)

        height = maxRow - minRow + 1
        width = maxCol - minCol + 1

        return height * width