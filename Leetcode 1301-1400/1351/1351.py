# Leetcode 1351: Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Solved on 28th of December, 2025
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        """
        Counts the number of negative numbers in a grid sorted in non-increasing order both row-wise and column-wise.

        :param grid: A list of lists of integers representing the grid.
        :return: The total count of negative numbers in the grid.
        """
        rowCount = len(grid)
        colCount = len(grid[0])
        currentRow = rowCount - 1
        currentCol = 0
        negativeCount = 0

        while currentRow >= 0 and currentCol < colCount:
            if grid[currentRow][currentCol] < 0:
                negativeCount += (colCount - currentCol)
                currentRow -= 1
            else:
                currentCol += 1

        return negativeCount