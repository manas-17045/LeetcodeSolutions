# Leetcode 3989: Maximum Consistent Columns in a Grid
# https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/
# Solved on 9th of August, 2026
class Solution:
    def maxConsistentColumns(self, grid: list[list[int]], limit: int) -> int:
        """
        Determines the maximum number of consistent columns in a grid.
        
        Args:
            grid: The grid of integers.
            limit: The limit for the difference between elements in a column.
        
        Returns:
            The maximum number of consistent columns.
        """
        numRows = len(grid)
        numCols = len(grid[0])
        dp = [1] * numCols

        for j in range(1, numCols):
            for i in range(j):
                isCompatible = True

                for r in range(numRows):
                    if abs(grid[r][j] - grid[r][i]) > limit:
                        isCompatible = False
                        break

                if isCompatible:
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1

        return max(dp)