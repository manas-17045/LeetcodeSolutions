# Leetcode 2435: Paths in Matrix Whose Sum Is Divisible by K
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
# Solved on 18th of October, 2025
class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        """
        Calculates the number of paths from the top-left cell to the bottom-right cell
        such that the sum of elements along the path is divisible by k.

        Args:
            grid: A 2D list of integers representing the grid.
            k: An integer. The sum of elements along a path must be divisible by k.
        Returns:
            The number of paths modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        # Initialize 3D dp array
        dp = [[[0] * k for _ in range(n)] for __ in range(m)]

        start_rem = grid[0][0] % k
        dp[0][0][start_rem] = 1

        for i in range(m):
            for j in range(n):
                # Skip the starting cell (already initialized)
                if i == 0 and j == 0:
                    continue
                val_rem = grid[i][j] % k
                cur = dp[i][j]

                # Take paths from top cell (i-1, j)
                if i > 0:
                    top = dp[i - 1][j]
                    # Propagate all remainders from top to current
                    for r in range(k):
                        cnt = top[r]
                        if cnt:
                            newr = (r + val_rem) % k
                            cur[newr] = (cur[newr] + cnt) % MOD

                # Take paths from left cell (i, j-1)
                if j > 0:
                    left = dp[i][j - 1]
                    for r in range(k):
                        cnt = left[r]
                        if cnt:
                            newr = (r + val_rem) % k
                            cur[newr] = (cur[newr] + cnt) % MOD

        return dp[m - 1][n - 1][0] % MOD