# Leetcode 2711: Difference of Number of Distinct Values on Diagonals
# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/
# Solved on 13th of September, 2025
class Solution:
    def differenceOfDistinctValues(self, grid: list[list[int]]) -> list[list[int]]:
        """
        Calculates the absolute difference between the number of distinct values in the top-left diagonal
        and the bottom-right diagonal for each cell in the given grid.
        :param grid: A list of lists of integers representing the input grid.
        :return: A list of lists of integers representing the answer grid.
        """

        numRows = len(grid)
        numCols = len(grid[0])

        answer = [[0] * numCols for _ in range(numRows)]

        for row in range(numRows):
            for col in range(numCols):
                topLeft = set()
                i = row - 1
                j = col - 1
                while i >= 0 and j >= 0:
                    topLeft.add(grid[i][j])
                    i -= 1
                    j -= 1

                bottomRight = set()
                i = row + 1
                j = col + 1
                while i < numRows and j < numCols:
                    bottomRight.add(grid[i][j])
                    i += 1
                    j += 1

                answer[row][col] = abs(len(topLeft) - len(bottomRight))

        return answer