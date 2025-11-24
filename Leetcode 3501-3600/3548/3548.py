# Leetcode 3548: Equal Sum Grid Partition II
# https://leetcode.com/problems/equal-sum-grid-partition-ii/
# Solved on 24th of November, 2025
from collections import Counter


class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        """
        Determines if a grid can be partitioned into two subgrids with equal sums by making at most two cuts.

        Args:
            grid: A list of lists of integers representing the grid.
        Returns:
            True if the grid can be partitioned into two subgrids with equal sums, False otherwise.
        """
        def checkCuts(currentGrid):
            m, n = len(currentGrid), len(currentGrid[0])
            bottomCounts = Counter()
            totalSum = 0

            for r in range(m):
                for c in range(n):
                    val = currentGrid[r][c]
                    bottomCounts[val] += 1
                    totalSum += val

            topCounts = Counter()
            topSum = 0

            for i in range(m - 1):
                rowSum = 0
                for c in range(n):
                    val = currentGrid[i][c]
                    topCounts[val] += 1
                    bottomCounts[val] -= 1
                    if bottomCounts[val] == 0:
                        del bottomCounts[val]
                    rowSum += val

                topSum += rowSum
                bottomSum = totalSum - topSum
                diff = topSum - bottomSum

                if diff == 0:
                    return True

                if diff > 0:
                    target = diff
                    if n == 1:
                        if currentGrid[0][0] == target or currentGrid[i][0] == target:
                            return True
                    elif i == 0:
                        if currentGrid[0][0] == target or currentGrid[0][n - 1] == target:
                            return True
                    else:
                        if topCounts[target] > 0:
                            return True
                else:
                    target = -diff
                    if n == 1:
                        if currentGrid[i + 1][0] == target or currentGrid[m - 1][0] == target:
                            return True
                    elif i == m - 2:
                        if currentGrid[m - 1][0] == target or currentGrid[m - 1][n - 1] == target:
                            return True
                    else:
                        if bottomCounts[target] > 0:
                            return True
            return False

        if checkCuts(grid):
            return True

        transposedGrid = [list(row) for row in zip(*grid)]
        if checkCuts(transposedGrid):
            return True

        return False