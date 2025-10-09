# Leetcode 3402: Minimum Operations to Make Columns Strictly Increasing
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/
# Solved on 9th of October, 2025
class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum operations needed to make each column in the grid strictly increasing.
        An operation consists of incrementing a cell's value by 1.

        Args:
            grid: A 2D list of integers representing the grid.
        Returns:
            The minimum number of operations required.
        """
        m = len(grid)
        n = len(grid[0])
        operations = 0

        # Process each column
        for j in range(n):
            # Process each row in the column (starting from row 1)
            for i in range(1, m):
                # If current element is noy strictly greater than previous
                if grid[i][j] <= grid[i-1][j]:
                    # Calculate operations needed
                    needed = grid[i - 1][j] + 1 - grid[i][j]
                    operations += needed
                    # Update the grid value
                    grid[i][j] = grid[i - 1][j] + 1

        return operations