# Leetcode 3393: Count Paths With the Given XOR Value
# https://leetcode.com/problems/count-paths-with-the-given-xor-value/
# Solved on 11th of September, 2025
class Solution:
    def countPathsWithXorValue(self, grid: list[list[int]], k: int) -> int:
        """
        Counts the number of paths from the top-left cell (0, 0) to the bottom-right cell (m-1, n-1)
        such that the XOR sum of all cell values along the path equals `k`.
        Only moves right or down are allowed.

        Args:
            grid (list[list[int]]): A 2D grid of integers.
            k (int): The target XOR sum.
        Returns:
            int: The number of paths with the target XOR sum.
        """
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        MAX_XOR = 16

        dp = [[[0] * MAX_XOR for _ in range(n)] for _ in range(m)]

        # Start
        start_x = grid[0][0]
        dp[0][0][start_x] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                # Collect ways from top and left
                if i > 0:
                    prev = dp[i - 1][j]
                    # For each possible previous xor, update current
                    for px in range(MAX_XOR):
                        cnt = prev[px]
                        if cnt:
                            dp[i][j][px ^ val] = (dp[i][j][px ^ val] + cnt) % MOD

                if j > 0:
                    prev = dp[i][j - 1]
                    for px in range(MAX_XOR):
                        cnt = prev[px]
                        if cnt:
                            dp[i][j][px ^ val] = (dp[i][j][px ^ val] + cnt) % MOD

        return dp[m - 1][n - 1][k] % MOD