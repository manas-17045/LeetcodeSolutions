# Leetcode 3148: Maximum Difference Score in a Grid
# https://leetcode.com/problems/maximum-difference-score-in-a-grid/
# Solved on 9th of December, 2025
class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum difference score in a given grid.

        Args:
            grid (list[list[int]]): The input grid of integers.
        Returns:
            int: The maximum difference score.
        """
        rows = len(grid)
        cols = len(grid[0])
        minValues = [float('inf')] * cols
        maxScore = float('-inf')

        for r in range(rows):
            for c in range(cols):
                minPrev = float('inf')

                if r > 0:
                    minPrev = min(minPrev, minValues[c])
                if c > 0:
                    minPrev = min(minPrev, minValues[c - 1])

                if minPrev != float('inf'):
                    maxScore = max(maxScore, grid[r][c] - minPrev)

                minValues[c] = min(minPrev, grid[r][c])

        return int(maxScore)