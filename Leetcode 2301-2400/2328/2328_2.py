# Leetcode 2328: Number of Increasing Paths in a Grid
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
# Solved on 8th of July, 2025
import sys
sys.setrecursionlimit(10**7)


class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        """
        Counts the number of strictly increasing paths in a grid.

        A path can start from any cell and move to an adjacent cell (up, down, left, or right)
        if the value of the adjacent cell is strictly greater than the current cell's value.

        Args:
            grid: A 2D list of integers representing the grid.
        Returns:
            The total number of strictly increasing paths modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        memo = [[0] * n for _ in range(m)]

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i: int, j: int) -> int:
            if memo[i][j]:
                return memo[i][j]
            cnt = 1
            val = grid[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > val:
                    cnt = (cnt + dfs(ni, nj)) % MOD
            memo[i][j] = cnt
            return cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % MOD

        return ans