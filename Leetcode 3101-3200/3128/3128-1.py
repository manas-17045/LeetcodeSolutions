# Leetcode 3128: Right Triangles
# https://leetcode.com/problems/right-triangles/
# Solved on 1st of October, 2025
class Solution:
    def numberOfRightTriangles(self, grid: list[list[int]]) -> int:
        """
        Calculates the number of right triangles that can be formed from '1's in a given grid.
        A right triangle is formed by three '1's where two sides are parallel to the grid axes.

        Args:
            grid: A 2D list of integers (0 or 1) representing the grid.
        Returns:
            The total number of right triangles.
        """
        if not grid or not grid[0]:
            return 0

        numRows = len(grid)
        numCols = len(grid[0])

        rowCounts = [0] * numRows
        colCounts = [0] * numCols

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1:
                    rowCounts[i] += 1
                    colCounts[j] += 1

        totalTriangles = 0
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1:
                    horizontalPoints = rowCounts[i] - 1
                    verticalPoints = colCounts[j] - 1
                    if horizontalPoints > 0 and verticalPoints > 0:
                        totalTriangles += horizontalPoints * verticalPoints

        return totalTriangles