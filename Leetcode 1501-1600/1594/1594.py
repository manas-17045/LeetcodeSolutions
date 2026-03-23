# Leetcode 1594: Maximum Non Negative Product in a Matrix
# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
# Solved on 23rd of March, 2026
class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        """
        Finds the maximum non-negative product of a path from the top-left to the bottom-right of a matrix.
        The path can only move right or down.

        :param grid: A 2D list of integers representing the matrix.
        :return: The maximum non-negative product modulo 10^9 + 7, or -1 if no non-negative product exists.
        """
        rowCount = len(grid)
        colCount = len(grid[0])

        maxRow = [0] * colCount
        minRow = [0] * colCount

        maxRow[0] = grid[0][0]
        minRow[0] = grid[0][0]
        for j in range(1, colCount):
            maxRow[j] = maxRow[j - 1] * grid[0][j]
            minRow[j] = minRow[j - 1] * grid[0][j]

        for i in range(1, rowCount):
            maxRow[0] *= grid[i][0]
            minRow[0] *= grid[i][0]

            for j in range(1, colCount):
                currVal = grid[i][j]
                prodOne = maxRow[j] * currVal
                prodTwo = minRow[j] * currVal
                prodThree = maxRow[j - 1] * currVal
                prodFour = minRow[j - 1] * currVal
                maxRow[j] = max(prodOne, prodTwo, prodThree, prodFour)
                minRow[j] = min(prodOne, prodTwo, prodThree, prodFour)

        finalAns = maxRow[-1]

        return -1 if finalAns < 0 else finalAns % 1_000_000_007