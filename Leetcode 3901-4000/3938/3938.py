# Leetcode 3938: Maximum Path Intersection Sum in a Grid
# https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/
# Solved on 7th of June, 2026
class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum path intersection sum in a given grid.

        :param grid: A 2D list of integers representing the grid.
        :return: An integer representing the maximum score calculated from path intersections.
        """
        numRows = len(grid)
        numCols = len(grid[0])
        maxSum = -float('inf')

        for rowIdx in range(numRows):
            if numCols >= 2:
                prevDp = grid[rowIdx][0] + grid[rowIdx][1]
                if prevDp > maxSum:
                    maxSum = prevDp
                prevVal = grid[rowIdx][1]

                for colIdx in range(2, numCols):
                    curDp = grid[rowIdx][colIdx] + (prevDp if prevDp > prevVal else prevVal)
                    if curDp > maxSum:
                        maxSum = curDp

                    prevDp = curDp
                    prevVal = grid[rowIdx][colIdx]

        for colIdx in range(numCols):
            if numRows >= 2:
                prevDp = grid[0][colIdx] + grid[1][colIdx]
                if prevDp > maxSum:
                    maxSum = prevDp
                prevVal = grid[1][colIdx]

                for rowIdx in range(2, numRows):
                    curDp = grid[rowIdx][colIdx] + (prevDp if prevDp > prevVal else prevVal)
                    if curDp > maxSum:
                        maxSum = curDp

                    prevDp = curDp
                    prevVal = grid[rowIdx][colIdx]

        for rowIdx in range(1, numRows - 1):
            for colIdx in range(1, numCols - 1):
                if grid[rowIdx][colIdx] > maxSum:
                    maxSum = grid[rowIdx][colIdx]

        return maxSum