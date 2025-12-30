# Leetcode 3546: Equal Sum Grid Partition I
# https://leetcode.com/problems/equal-sum-grid-partition-i/
# Solved on 30th of December, 2025
class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        """
        Determines if a grid can be partitioned into two sub-grids with equal sums.
        A partition can be made either by a horizontal cut or a vertical cut.

        Args:
            grid (list[list[int]]): The input grid of integers.
        Returns:
            bool: True if the grid can be partitioned into two equal sum parts, False otherwise.
        """
        totalSum = 0
        for row in grid:
            totalSum += sum(row)

        if totalSum % 2 != 0:
            return False

        target = totalSum // 2

        currentSum = 0
        for row in grid:
            currentSum += sum(row)
            if currentSum == target:
                return True
            if currentSum > target:
                break

        rows = len(grid)
        cols = len(grid[0])
        currentSum = 0

        for j in range(cols):
            colSum = 0
            for i in range(rows):
                colSum += grid[i][j]
            currentSum += colSum

            if currentSum == target:
                return True
            if currentSum > target:
                break

        return False