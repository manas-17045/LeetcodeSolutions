# Leetcode 1568: Minimum Number of Days to Disconnect Island
# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
# Solved on 14th of October, 2025
class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum number of days to disconnect a grid of land and water cells.
        :param grid: A 2D list of integers representing the grid, where 1 is land and 0 is water.
        :return: The minimum number of days (0, 1, or 2) to disconnect the grid.
        """
        def count_islands(g):
            visited = set()
            count = 0

            def dfs(i, j):
                if i < 0 or i >= len(g) or j < 0 or j >= len(g[0]):
                    return
                if (i, j) in visited or g[i][j] == 0:
                    return
                visited.add((i, j))
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

            for i in range(len(g)):
                for j in range(len(g[0])):
                    if g[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j)
                        count += 1

            return count

        def is_disconnected(g):
            islands = count_islands(g)
            return islands != 1

        # Check if already disconnected
        if is_disconnected(grid):
            return 0

        # Try removing each land cell and check if disconnected
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_disconnected(grid):
                        grid[i][j] = 1
                        return 1
                    grid[i][j] = 1

        # If we can't disconnect in 1 day, answer is 2
        return 2