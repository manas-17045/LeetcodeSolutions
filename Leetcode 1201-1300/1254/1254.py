# Leetcode 1254: Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/
# Solved on 25th of October, 2026
class Solution:
    def closedIslands(self, grid: list[list[int]]) -> int:
        """
        Calculates the total number of closed islands in a 2D grid.

        Parameters:
            grid (list[list[int]]): A 2D grid where 0 represents land and 1 represents water.

        Returns:
            int: The number of islands completely surrounded by water.
        """
        rowCount = len(grid)
        colCount = len(grid[0])
        closedIslandCount = 0

        def floodFill(startRow: int, startCol: int) -> None:
            cellStack = [(startRow, startCol)]
            grid[startRow][startCol] = 1

            while cellStack:
                currentRow, currentCol = cellStack.pop()
                for deltaRow, deltaCol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighborRow = currentRow + deltaRow
                    neighborCol = currentCol + deltaCol

                    if 0 <= neighborRow < rowCount and 0 <= neighborCol < colCount and grid[neighborRow][neighborCol] == 0:
                        grid[neighborRow][neighborCol] = 1
                        cellStack.append((neighborRow, neighborCol))

        for rowIndex in range(rowCount):
            if grid[rowIndex][0] == 0:
                floodFill(rowIndex, 0)
            if grid[rowIndex][colCount - 1] == 0:
                floodFill(rowIndex, colCount - 1)

        for colIndex in range(colCount):
            if grid[0][colIndex] == 0:
                floodFill(0, colIndex)
            if grid[rowCount - 1][colIndex] == 0:
                floodFill(rowCount - 1, colIndex)

        for rowIndex in range(1, rowCount - 1):
            for colIndex in range(1, colCount - 1):
                if grid[rowIndex][colIndex] == 0:
                    closedIslandCount += 1
                    floodFill(rowIndex, colIndex)

        return closedIslandCount