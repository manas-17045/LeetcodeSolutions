# Leetcode 2435: Paths in Matrix Whose Sum Is Divisible by K
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
# Solved on 18th of October, 2025
class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        """
        Calculates the number of paths from the top-left to the bottom-right of a grid
        such that the sum of elements along the path is divisible by k.

        Args:
            grid: A 2D list of integers representing the grid.
            k: An integer representing the divisor.

        Returns:
            The number of paths whose sum is divisible by k, modulo 10^9 + 7.
        """
        numRows = len(grid)
        numCols = len(grid[0])
        mod = 10**9 + 7

        dpTable = [[[0] * k for _ in range(numCols)] for _ in range(numRows)]

        dpTable[0][0][grid[0][0] % k] = 1

        for r in range(numRows):
            for c in range(numCols):
                currentVal = grid[r][c]
                for rem in range(k):
                    prevRem = (rem - currentVal) % k

                    pathsFromAbove = 0
                    if r > 0:
                        pathsFromAbove = dpTable[r - 1][c][prevRem]

                    pathsFromLeft = 0
                    if c > 0:
                        pathsFromLeft = dpTable[r][c - 1][prevRem]

                    if r > 0 or c > 0:
                        dpTable[r][c][rem] = (pathsFromAbove + pathsFromLeft) % mod

        return dpTable[numRows - 1][numCols - 1][0]