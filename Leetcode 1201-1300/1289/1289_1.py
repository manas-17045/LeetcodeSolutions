# Leetcode 1289: Minimum Falling Path Sum II
# https://leetcode.com/problems/minimum-falling-path-sum-ii/
# Solved on 15th of June, 2025

class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum falling path sum in a square grid where you cannot
        choose the same column in consecutive rows.

        Args:
            grid: A square grid of integers.

        Returns:
            The minimum falling path sum.
        """
        n = len(grid)

        if n == 1:
            return grid[0][0]

        for i in range(1, n):
            firstMin = float('inf')
            secondMin = float('inf')
            firstMinIndex = -1

            for j in range(n):
                value = grid[i - 1][j]
                if value < firstMin:
                    secondMin = firstMin
                    firstMin = value
                    firstMinIndex = j
                elif value < secondMin:
                    secondMin = value

            for j in range(n):
                if j == firstMinIndex:
                    grid[i][j] += secondMin
                else:
                    grid[i][j] += firstMin

        return min(grid[n - 1])