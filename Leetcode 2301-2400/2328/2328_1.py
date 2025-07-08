# Leetcode 2328: Number of Increasing Paths in a Grid
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
# Solved on 8th of July, 2025
class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        """
        Counts the number of strictly increasing paths in a given grid.

        A path can start from any cell and move to an adjacent cell (up, down, left, or right)
        if the value of the destination cell is strictly greater than the current cell.

        Args:
            grid: A 2D list of integers representing the grid.

        Returns:
            The total number of increasing paths modulo 10^9 + 7.
        """

        rows = len(grid)
        cols = len(grid[0])
        modulo = 10**9 + 7

        memo = [[0] * cols for _ in range(rows)]

        def dfs(row, col):
            if memo[row][col] != 0:
                return memo[row][col]

            pathCount = 1

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                newRow, newCol = (row + dr), (col + dc)

                if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] > grid[row][col]:
                    pathCount = (pathCount + dfs(newRow, newCol)) % modulo

            memo[row][col] = pathCount
            return pathCount

        totalPaths = 0
        for r in range(rows):
            for c in range(cols):
                totalPaths = (totalPaths + dfs(r, c)) % modulo

        return totalPaths