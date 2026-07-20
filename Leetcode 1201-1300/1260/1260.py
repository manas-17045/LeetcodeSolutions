# Leetcode 1260: Shift 2D Grid
# https://leetcode.com/problems/shift-2d-grid/
# Solved on 20th of July, 2026
class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        Shifts the 2D grid by k positions.
        @param grid: The 2D grid.
        @param k: The number of positions to shift.
        @return: The shifted 2D grid.
        """
        rowCount = len(grid)
        colCount = len(grid[0])
        totalElements = rowCount * colCount
        effectiveShift = k % totalElements

        resultGrid = [[0] * colCount for _ in range(rowCount)]

        for rowIndex in range(rowCount):
            for colIndex in range(colCount):
                currentIndex = rowIndex * colCount + colIndex
                previousIndex = (currentIndex - effectiveShift) % totalElements
                resultGrid[rowIndex][colIndex] = grid[previousIndex // colCount][previousIndex % colCount]
        
        return resultGrid