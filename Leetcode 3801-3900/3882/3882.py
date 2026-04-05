# Leetcode 3882: Minimum XOR Path in a Grid
# https://leetcode.com/problems/minimum-xor-path-in-agrid/
# Solved on 5th of April, 2026
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        """
        Finds the minimum XOR sum path from the top-left to the bottom-right of a grid.
        The path can only move down or right.

        :param grid: A 2D list of integers representing the grid.
        :return: The minimum possible XOR sum of all elements along a path.
        """
        numRows = len(grid)
        numCols = len(grid[0])
        prevRow = [set() for _ in range(numCols)]
        prevRow[0].add(grid[0][0])

        for colIdx in range(1, numCols):
            for val in prevRow[colIdx - 1]:
                prevRow[colIdx].add(val ^ grid[0][colIdx])

        for rowIdx in range(1, numRows):
            currRow = [set() for _ in range(numCols)]
            for val in prevRow[0]:
                currRow[0].add(val ^ grid[rowIdx][0])

            for colIdx in range(1, numCols):
                cellVal = grid[rowIdx][colIdx]
                for val in prevRow[colIdx]:
                    currRow[colIdx].add(val ^ cellVal)
                for val in currRow[colIdx - 1]:
                    currRow[colIdx].add(val ^ cellVal)

            prevRow = currRow

        return min(prevRow[-1])